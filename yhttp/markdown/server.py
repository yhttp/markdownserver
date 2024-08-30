import os
from wsgiref.simple_server import make_server

import easycli
import sass as libsass
from mako.lookup import TemplateLookup
import yhttp.core as y

from . import __version__, toc
from .settings import settings
from .markdown import markdowner


here = os.path.dirname(__file__)
app = y.Application(version=__version__)


@app.when
def ready(app):
    if 'yhttp' in settings:
        app.settings.merge(settings.server)

    app.loopkup = TemplateLookup(
        directories=[here],
        cache_enabled=not settings.yhttp.debug,
    )


def sasscompile(s):
    return libsass.compile(
        indented=True,
        string=s,
        include_paths=[os.path.join(here, 'styles')],
        source_comments=False,
    )


sass = y.utf8('text/css', dump=sasscompile)


# TODO: cache
@app.route('/index.css')
@sass
def get(req, path=None):
    with open(os.path.join(here, 'styles/index.sass')) as f:
        return f.read()


@app.route(r'/webmanifest\.json')
@y.json
def get(req):
    return dict(
        icons=[
            dict(
                src=f'{app.metapath}/android-chrome-192x192.png',
                type='image/png',
                sizes='192x192'
            ),
            dict(
                src=f'{app.metapath}/android-chrome-512x512.png',
                type='image/png',
                sizes='512x512'
            )
        ]
    )


@y.html
def get(req, path=None):
    # FIXME: (security) prevent to get parent directories
    targetpath = os.path.join(settings.server.root, path or '')
    targetfile = None

    # Default document
    default = settings.server.default_document
    if os.path.isdir(targetpath):
        if default:
            default = os.path.join(targetpath, default)
            if os.path.isfile(default):
                targetfile = default

    else:
        targetfile = targetpath
        targetpath = os.path.dirname(targetpath)

    # Fallback
    if not targetfile or not os.path.isfile(targetfile):
        fallback = settings.server.fallback_document
        if fallback:
            fallback = os.path.join(settings.server.root, fallback)
            if os.path.exists(fallback):
                targetfile = fallback

    # 404 not found
    if not targetfile or not os.path.isfile(targetfile):
        if not os.path.isdir(targetpath):
            raise y.statuses.notfound()

        targetfile = None

    # Generate TOC
    headings, subdirs = toc.extractdir(targetpath, '', settings.toc.depth)
    t = app.loopkup.get_template('master.mako')

    renderargs = dict(
        title=settings.server.title,
        hometitle='Home',
        toc=headings,
        subdirs=subdirs,
        metapath=app.metapath,
        paths=os.path.dirname(path).split('/') if path else [],
    )
    if not targetfile:
        return t.render(content='', **renderargs)
        return

    with open(targetfile) as f:
        return t.render(content=markdowner.convert(f.read()), **renderargs)


class Serve(easycli.SubCommand):
    _default_bind = '8080'
    __command__ = 'serve'
    __aliases__ = ['s']
    __arguments__ = [
        easycli.Argument(
            '-b', '--bind',
            default=_default_bind,
            metavar='{HOST:}PORT',
            help='Bind Address. default: %s' % _default_bind
        ),
    ]

    def __call__(self, args):  # pragma: no cover
        """the no cover pragma was set, because the coverae meassurement in
        subprocess is so complicated, but this function is covered by
        test_builtincli.py.
        """
        host, port = args.bind.split(':')\
            if ':' in args.bind else ('localhost', args.bind)

        # metadata (favicon, logo and etc)
        metadir = os.path.join(args.directory, '.ymdmetadata')
        if not os.path.isdir(metadir):
            metadir = os.path.join(here, 'defaultmetadata')

        app.metapath = '/.ymdmetadata'
        app.staticdirectory(
            r'/\.ymdmetadata/',
            metadir,
            default=False,
            autoindex=False,
        )

        app.staticdirectory(
            r'/static/',
            os.path.join(here, 'static/'),
            default=False,
            autoindex=False,
        )
        app.route('/(.*)')(get)
        app.ready()

        httpd = make_server(host, int(port), app)
        print(f'Markdown server started at http://{host}:{port}')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("CTRL+C pressed.")
            app.shutdown()
