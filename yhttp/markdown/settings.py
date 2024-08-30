import pymlconf


_builtinsettings = '''
yhttp:
    debug: false

server:
    default_document: index.md
    fallback_document: notfound.md


root: .
title: HTTP Markdown Server
toc:
    depth: 3


# a list of regex patterns to exclude from TOC and HTTP serve
exclude:

'''


settings = pymlconf.Root(_builtinsettings)


def init(configfile=None):
    global settings

    if configfile:
        settings.loadfile(configfile)
