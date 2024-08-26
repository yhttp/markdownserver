import os
import sys
from wsgiref.simple_server import make_server

import pymlconf
import easycli

from . import settings, __version__
from .server import Serve


class Main(easycli.Root):
    __completion__ = True
    __help__ = f'{sys.argv[0]} command line interface.'
    __arguments__ = [
        easycli.Argument('--version', action='store_true'),
        easycli.Argument(
            '-c', '--configuration-file',
            metavar="FILE",
            dest='configurationfile',
            help='Configuration file',
        ),
        Serve,
    ]


    def _execute_subcommand(self, args):
        if args.configurationfile:
            settings.init(args.configurationfile)

        return super()._execute_subcommand(args)

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        self._parser.print_help()
