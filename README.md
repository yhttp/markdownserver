# markdownserver
[![PyPI](http://img.shields.io/pypi/v/yhttp-markdown.svg)](https://pypi.python.org/pypi/yhttp-markdown)
[![Build](https://github.com/yhttp/markdown/actions/workflows/build.yml/badge.svg)](https://github.com/yhttp/markdown/actions/workflows/build.yml)
[![Coverage Status](https://coveralls.io/repos/github/yhttp/markdown/badge.svg?branch=master)](https://coveralls.io/github/yhttp/markdown?branch=master)
[![Python](https://img.shields.io/badge/Python-%3E%3D3.10-blue)](https://python.org)

Markdown server using yhttp.


## Features

- Serve a directory of markdown files and subdirectories as HTML using
    [markdown2](https://github.com/trentm/python-markdown2).
- Personalizable favicon, touch-icon logo and etc.
- Syntaxt highlighting for code blocks + themes using
    [pygment](https://pygments.org/).
- Copy-to-clipboard buttons for code-blocks and HTML bookmarks.
- Resizable sidebat and page layout powered by CSS Flexbox.
- Breadcrumbs (path) navigator.
- Change configuration using file and command line interface.

## Install
```bash
pip install yhttp-markdown
```

## Quickstart
Navugate to a directory of markdown files, then:
```bash
yhttp-markdown serve
```

## Command line interface
```bash
yhttp-markdown --help
```

```bash
usage: yhttp-markdown [-h] [-c FILE] [-C DIRECTORY] [-O OPTION] [--version]
                      {serve,s,completion} ...

options:
  -h, --help            show this help message and exit
  -c FILE, --configuration-file FILE
                        Configuration file
  -C DIRECTORY, --directory DIRECTORY
                        Change to this path before starting, default is: `.`
  -O OPTION, --option OPTION
                        Set a configutation entry: -O foo.bar.baz='qux'. this
                        argument can passed multiple times.
  --version

Sub commands:
  {serve,s,completion}
    serve (s)
    completion          Bash auto completion using argcomplete python package.
```

### Bash auto completion 
To enable bash auto comletion, first run this command:
```bash
yhttp-markdown completion install
```

Then close and re-open your shell or deactivate/activate the current virtual
environment (if using) to apply the change:
```bash
deactivate && . activate.sh
```

Test it:
```bash
yhttp-markdown TAB TAB
```


## Configuration

`yhttp-markdown` can be configured using a YAML configuration file 
(the `-c/--configuration-file` and `-O/--option` flags.

```bash
yhttp-markdown -c settings.yaml -O highlight.theme=vim serve
```

This is the  example of default configuration file:
```yaml
# yhttp debug flag
debug: false


# app specific
default: index.md
root: .


# site title
title: HTTP Markdown Server
toc:
    depth: 3


# a list of regex patterns to exclude from TOC and HTTP serve
exclude:


# mako templates
markdown_template: default.mako
notfound_template: notfound.mako


# metadata path
metadata:
    physical: .ymdmetadata
    baseurl: /.ymdmetadata


# syntaxt highlighting theme
highlight:
    theme: monokai
```


## Syntax highlighting

## Contribuition
