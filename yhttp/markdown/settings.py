import pymlconf


settings = None
_builtinsettings = '''
yhttp:
    debug: false
'''


def init(configfile=None):
    global settings
    settings = pymlconf.Root(self._builtinsettings)

    if configfile:
        settings.loadfile(configfile)
