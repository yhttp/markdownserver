# yhttp markdown server

## Install
```bash
pip install yhttp-markdown
```

## Usage
Navigate to a directory containing markdown files and similar sub-directories,
then run:

```bash
yhttp-markdown serve
```

```python
import os
import sys

import easycli

from . import __version__
from .server import app, Serve


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
        easycli.Argument(
            '-C', '--directory',
            metavar="DIRECTORY",
            default='.',
            help='Change to this path before starting, default is: `.`'
        ),
        Serve,
    ]

    def _execute_subcommand(self, args):  # pragma: no cover
        if args.directory != '.':
            os.chdir(args.directory)

        if args.configurationfile:
            app.settings.loadfile(args.configurationfile)

        return super()._execute_subcommand(args)

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        self._parser.print_help()
```
