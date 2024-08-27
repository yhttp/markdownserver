import pymlconf


_builtinsettings = '''
yhttp:
    debug: false

server:
    title: Markdown Server
    default_document: index.md
    fallback_document: notfound.md
    root: .
'''


settings = pymlconf.Root(_builtinsettings)


def init(configfile=None):
    global settings

    if configfile:
        settings.loadfile(configfile)