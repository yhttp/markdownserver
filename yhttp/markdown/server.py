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
cfg = app.settings


# Builtin configuration
cfg.merge('''
# yhttp debug flag
debug: true

# app specific
default: index.md
root: .

title: HTTP Markdown Server
toc:
    depth: 3


# a list of regex patterns to exclude from TOC and HTTP serve
exclude:

# templates
markdown_template: default.mako
notfound_template: notfound.mako

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
    baseurl = cfg.metadata.baseurl
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


def notfound(req, path, **kw):
    template = app.loopkup.get_template(cfg.notfound_template)
    req.response.status = y.statuses.notfound().status
    return template.render(filename=path, **kw)


@y.html
def get(req, path=None):
    # FIXME: (security) prevent to get parent directories
    targetpath = os.path.join(cfg.root, path or '')
    targetfile = None

    renderargs = dict(
        title=cfg.title,
        toc=[],
        subdirs=[],
        metapath=cfg.metadata.baseurl,
        paths=os.path.dirname(path).split('/') if path else [],
    )

    # Check exclusiono
    for pat in app.excludes:
        if pat.match(path):
            return notfound(req, path, **renderargs)

    # Default document
    default = cfg.default
    if os.path.isdir(targetpath):
        if default:
            default = os.path.join(targetpath, default)
            if os.path.isfile(default):
                targetfile = default

    else:
        targetfile = targetpath
        targetpath = os.path.dirname(targetpath)

    if os.path.exists(targetpath):
        # Generate TOC
        headings, subdirs = toc.extractdir(targetpath, '', cfg.toc.depth)
        renderargs['toc'] = headings
        renderargs['subdirs'] = subdirs

    # 404 not found
    if not targetfile or not os.path.isfile(targetfile):
        return notfound(req, path, **renderargs)

    template = app.loopkup.get_template(cfg.markdown_template)
    with open(targetfile) as f:
        return template.render(
            content=markdowner.convert(f.read()),
            **renderargs
        )


@app.when
def ready(app):
    app.excludes = [re.compile(p) for p in cfg.exclude or []]
    app.loopkup = TemplateLookup(
        directories=[os.path.join(here, 'templates')],
        cache_enabled=not cfg.debug,
    )

    app.staticdirectory(
        cfg.metadata.baseurl.replace('.', r'\.') + '/',
        cfg.metadata.physical,
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
        cfg.metadata.baseurl.replace('.', r'\.') + '/(.*)',
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
        if not os.path.isdir(cfg.metadata.physical):
            cfg.metadata.physical = os.path.join(here, 'defaultmetadata')

        app.ready()
        httpd = make_server(host, int(port), app)
        print(f'Markdown server started at http://{host}:{port}')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("CTRL+C pressed.")
            app.shutdown()
