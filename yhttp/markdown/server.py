import os

import easycli
from yhttp.core import Application, static

from . import __version__
from .decorator import markdown2html


app = Application(version=__version__)


# Builtin configuration
# app.settings.merge('''
# ''')


app.route(f'/(.*)')(
    markdown2html(cssfiles=['main.css'])(
        static.directory(
            rootpath=os.curdir,
            default='index.md',
            autoindex=True,
            fallback=False
        )
    )
)


DEFAULT_ADDRESS = '8080'


class Serve(easycli.SubCommand):
    __command__ = 'serve'
    __aliases__ = ['s']
    __arguments__ = [
        easycli.Argument(
            '-b', '--bind',
            default=DEFAULT_ADDRESS,
            metavar='{HOST:}PORT',
            help='Bind Address. default: %s' % DEFAULT_ADDRESS
        ),
        easycli.Argument(
            '-C',
            '--directory',
            default='.',
            help='Change to this path before starting, default is: `.`'
        )
    ]

    def __call__(self, args):  # pragma: no cover
        """the no cover pragma was set, because the coverae meassurement in
        subprocess is so complicated, but this function is covered by
        test_builtincli.py.
        """
        host, port = args.bind.split(':')\
            if ':' in args.bind else ('localhost', args.bind)

        if args.directory != '.':
            os.chdir(args.directory)

        app.ready()
        httpd = make_server(host, int(port), app)
        print(f'Markdown server started at http://{host}:{port}')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("CTRL+C pressed.")
            app.shutdown()
