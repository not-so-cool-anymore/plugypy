import json
from .plugypy_errors import  InvalidConfigurationFile

class Configuration(object):
    load_all: bool
    plugins: dict

    def __init__(self, plugins: dict, load_all: bool):
        self.plugins = plugins
        self.load_all = load_all

class ConfigurationDeserializer():
    def __init__(self, config_file_location):
        self.__config_file_location =  config_file_location
    
    def deserialize_config(self):
        config = None

        with open(self.__config_file_location, 'r') as config_file:
            try:
                config_json = json.loads(config_file.read())
                config = Configuration(**config_json)
            except: 
                raise InvalidConfigurationFile() from None

        return config
