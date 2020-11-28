
class Configuration(object):
    will_load_all: bool
    plugins: dict

    def __init__(self, plugins: dict, will_load_all: bool):
        self.plugins = plugins
        self.wil_load_all = will_load_all