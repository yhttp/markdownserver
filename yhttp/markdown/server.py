import os
import re
from wsgiref.simple_server import make_server

import easycli
import sass as libsass
from mako.lookup import TemplateLookup
import yhttp.core as y

from . import __version__, toc
from .markdown import markdowner


here = os.path.dirname(__file__)
app = y.Application(version=__version__)


# Builtin configuration
app.settings.merge('''
# yhttp debug flag
debug: true

# app specific
default: index.md
fallback: index.md
root: .

title: HTTP Markdown Server
toc:
    depth: 3


# a list of regex patterns to exclude from TOC and HTTP serve
exclude:

# template
template: default.mako

# metadata path
metadata:
    physical: .ymdmetadata
    baseurl: /.ymdmetadata

''')


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
    baseurl = app.settings.metadata.baseurl
    return dict(
        icons=[
            dict(
                src=f'{baseurl}/android-chrome-192x192.png',
                type='image/png',
                sizes='192x192'
            ),
            dict(
                src=f'{baseurl}/android-chrome-512x512.png',
                type='image/png',
                sizes='512x512'
            )
        ]
    )


@y.html
def get(req, path=None):
    # FIXME: (security) prevent to get parent directories
    curpath = os.path.dirname(path) if path else '/'
    targetpath = os.path.join(app.settings.root, path or '')
    targetfile = None

    # Check exclusiono
    for pat in app.excludes:
        if pat.match(path):
            raise y.statuses.notfound()

    # Default document
    default = app.settings.default
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
        fallback = app.settings.fallback
        if fallback:
            fallback = os.path.join(app.settings.root, curpath, fallback)
            if os.path.exists(fallback):
                raise y.statuses.found(app.settings.fallback)

            fallback = os.path.join(app.settings.root, app.settings.fallback)
            if os.path.exists(fallback):
                redurl = os.path.join('/', app.settings.fallback)
                raise y.statuses.found(redurl)

    # 404 not found
    if not targetfile or not os.path.isfile(targetfile):
        if not os.path.isdir(targetpath):
            raise y.statuses.notfound()

        targetfile = None

    # Generate TOC
    headings, subdirs = toc.extractdir(targetpath, '', app.settings.toc.depth)
    t = app.loopkup.get_template(app.settings.template)

    renderargs = dict(
        title=app.settings.title,
        hometitle='Home',
        toc=headings,
        subdirs=subdirs,
        metapath=app.settings.metadata.baseurl,
        paths=os.path.dirname(path).split('/') if path else [],
    )
    if not targetfile:
        return t.render(content='', **renderargs)
        return

    with open(targetfile) as f:
        return t.render(content=markdowner.convert(f.read()), **renderargs)


@app.when
def ready(app):
    app.excludes = [re.compile(p) for p in app.settings.exclude or []]
    app.loopkup = TemplateLookup(
        directories=[os.path.join(here, 'templates')],
        cache_enabled=not app.settings.debug,
    )

    app.staticdirectory(
        app.settings.metadata.baseurl.replace('.', r'\.') + '/',
        app.settings.metadata.physical,
        default=False,
        autoindex=False,
    )

    app.staticdirectory(
        r'/static/',
        os.path.join(here, 'static/'),
        default=False,
        autoindex=False,
    )

    # default handler
    app.route('/(.*)')(get)


@app.when
def shutdown(app):
    app.delete_route(
        app.settings.metadata.baseurl.replace('.', r'\.') + '/(.*)',
        'get'
    )

    app.delete_route(r'/static/(.*)', 'get')
    app.delete_route('/(.*)', 'get')


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
        meta = app.settings.metadata
        if not os.path.isdir(meta.physical):
            meta.physical = os.path.join(here, 'defaultmetadata')

        app.ready()
        httpd = make_server(host, int(port), app)
        print(f'Markdown server started at http://{host}:{port}')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("CTRL+C pressed.")
            app.shutdown()
