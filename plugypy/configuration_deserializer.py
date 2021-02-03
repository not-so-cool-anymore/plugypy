import json
from .plugypy_errors import InvalidConfigurationFile
from .configuration import Configuration
from .plugin import Plugin


class ConfigurationDeserializer():
    def __init__(self, config_file_location):
        self.__config_file_location = config_file_location

    def deserialize_config(self):
        config = None

        with open(self.__config_file_location, 'r') as config_file:
            plugins_list = list()

            try:
                config_json = json.loads(config_file.read())

                for _plugin in config_json['plugins']:
                    plugin = Plugin(
                        _plugin['name'],
                        _plugin['is_enabled']
                    )

                    plugins_list.append(plugin)

                config = Configuration(
                    config_json['will_load_all'],
                    plugins_list
                )
            except:
                raise InvalidConfigurationFile() from None

        return config
