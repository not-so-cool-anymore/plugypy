from typing import List
from .plugin import Plugin

class Configuration(object):
    will_load_all: bool
    plugins: List[Plugin]

    def __init__(self, plugins: List[Plugin], will_load_all: bool):
        self.plugins = plugins
        self.wil_load_all = will_load_all