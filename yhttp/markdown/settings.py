import pymlconf


_builtinsettings = '''
yhttp:
    debug: false
'''


settings = pymlconf.Root(_builtinsettings)


def init(configfile=None):
    global settings

    if configfile:
        settings.loadfile(configfile)
