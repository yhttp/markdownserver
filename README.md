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
- Resizable sidebar and page layout powered by CSS Flexbox.
- Breadcrumbs (path) navigator.
- Change configuration using file and command line interface.
- [mermaid](https://mermaid.js.org/) support.


![yhttp-markdown](https://raw.githubusercontent.com/yhttp/markdown/master/examples/screenshot.png)


## Install
```bash
pip install yhttp-markdown
```

## Quickstart
Navigate to a directory consist of markdown files, then:
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


### Nginx + Systemd + Gunicorn
Copy the `deploy.sh` to target server. then execute the script and answer the
questions.

```bash
bob@laptop:~$ scp deploy.sh <server>
bob@laptop:~$ ssh root@<server>
root@server:~# ./deploy.sh
```


## Configuration

`yhttp-markdown` can be configured using a YAML configuration file 
(the `-c/--configuration-file`) and `-O/--option` flags at the same time:

```bash
yhttp-markdown -c settings.yaml -O highlight.theme=vim -O toc.depth=2 serve
```

### Configuration file
This is the  example of default configuration file:

```yaml
# settings.yaml


# app specific
default: index.md
root: .


# site title
title: HTTP Markdown Server


# table of contents
toc:
  depth: 3


# a list of regex patterns to exclude from TOC and HTTP serve
exclude:


# metadata path
metadata:
  physical: .ymdmetadata
  baseurl: /.ymdmetadata


# syntaxt highlighting theme
highlight:
  theme: monokai
```


### Root directory
By default, `yhttp-markdown` serves files from the current directory (`pwd`).
you may navigate to desired path before running the `yhttp-markdown` command
or set the `root` configuration entry:

```yaml
# settings.yaml

root: path/to/www/root
```

```bash
yhttp-markdown -O root=/path/to/www/root serve
```


You may also use the `-C/--directory` command line option to `cd` to a 
directory before running the server.
```bash
yhttp-markdown -C /path/to/www/root serve
```

### Default document
`yhttp-markdown` looks for the `index.md` on requests referring to a 
directory (http://example.com/foo/). but, this can be changed using the 
`default` configuration entry:

```yaml
# settings.yaml

default: default.md
```

Or, using the command line interface:
```bash
yhttp-markdown -O default=default.md serve
```


### Table of contents
`yhttp-markdown` crawls the `*.md` files and finds the markdown headdings:

```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

To genrate a tree of HTTP bookmarks and table of contents section of the 
current requested path.

You can change the `toc.depth` configuration value to change the behaviour:
```bash
yhttp-markdown -Otoc.depth=3 serve
```


### Exclusion
To exclude file and directories from serving use the `exclude` configuration 
entry. it's a collection of regular expression patterns relative to the sites
root (`/`):

```yaml
# settings.yaml

exclude:
  - foo\\.md
  - bar/?.*
```

Or, using the command line interface:
```bash
yhttp-markdown -O"exclude=[lorem\.md, bar/?.*]" serve
```


### Site metadata
The default website metadata such as `favicon` and `logo` could be overriden 
using the `.ymdmetadata` directory. this directory must be placed dirctly 
inside the `root`. so, these resources will be available at 
`http://localhost:8080/.ymdmetadata/` when the server is running.

This is an examples of the metadata directory.
```
.ymdmetadata/
  android-chrome-192x192.png
  android-chrome-512x512.png
  apple-touch-icon.png
  favicon-16x16.png
  favicon-32x32.png
  favicon.ico
  logo.svg
```

The name and base path are also changable using the `metadata.physical` and
`metadata.baseurl` configuration entries:
```yaml
# settings.yaml

metadata:
  physical: .ymdmetadata
  baseurl: /.ymdmetadata
```


### Code blocks syntax highlighting
`yhttp-markdown` uses the
[fenced-code-blocks](https://github.com/trentm/python-markdown2/wiki/fenced-code-blocks)
and [pygment](https://pygments.org/) to make the code blocks prettier.

The pygment theme can be changed using the `highlight.theme` configuration
entry:

```yaml
# settings.yaml

highlight:
  theme: monokai
```

Or, using the command line interface:
```bash
yhttp-markdown -O highlight.theme=vim serve
```

Available themes: 

- autumn
- borland
- bw
- colorful
- default
- emacs
- friendly
- fruity
- manni
- monokai
- murphy
- native
- pastie
- perldoc
- tango
- trac
- vim
- vs

See [pygments styles page](https://pygments.org/styles/) to figure out how 
they looks like.


## Contribuition

### Setup development environment

Install [python-makelib](https://github.com/pylover/python-makelib), then:
```bash
cd path/to/yhttp-markdown
make fresh env activate.sh
```

### Test and coverage
```bash
make test
make cover
```

### Lint
```bash
make lint
```


### Serve
```bash
make serve
```

Or
```bash
source activate.sh
yhttp-markdown -C examples serve
```


> **_NOTE:_**  Do a `make qa` or `make cover lint` before commit.
