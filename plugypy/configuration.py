from typing import List
from .plugin import Plugin


class Configuration(object):
    will_load_all: bool
    plugins: List[Plugin]

    def __init__(self, will_load_all: bool, plugins: List[Plugin]):
        self.will_load_all = will_load_all
        self.plugins = plugins

    def __str__(self):
        configuration_string = 'PlugyPy Plugins Configuration:\n'
        configuration_string += '\tWill Load All Plugins: {}\n'.format(
            self.will_load_all)

        for plugin in self.plugins:
            configuration_string += '\t\tPlugin Name: {}\n'.format(plugin.name)
            configuration_string += '\t\tIs Enabled: {}\n'.format(
                plugin.is_enabled)

        return configuration_string
