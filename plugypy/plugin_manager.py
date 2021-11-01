import os
import sys
import json
from .plugypy_errors import FunctionNotFoundError
from .configuration_deserializer import ConfigurationDeserializer, Configuration


class PluginManager():
    __configuration: Configuration

    def __init__(self, plugins_folder_location: str, configuration: Configuration, will_verify_ownership=False):
        self.__plugins_folder_location = plugins_folder_location
        self.__configuration = configuration
        self.__will_verify_plugins_ownership = will_verify_ownership

    def discover_plugins(self) -> list:
        plugins = list()
        plugins_directory_content = os.listdir(self.__plugins_folder_location)

        for content in plugins_directory_content:
            content_location = self.__plugins_folder_location + '/' + content

            if (os.path.isdir(content_location) or content == '__init__.py' or content.endswith('.json')):
                continue

            # if self.__will_verify_plugins_ownership and not self.__verify_plugin_ownership(content_location):
            #    continue

            plugins.append(content.replace('.py', ''))
        return plugins

    def import_plugins(self, plugins_list):
        loaded_plugins = list()
        sys.path.insert(1, self.__plugins_folder_location)

        for plugin in plugins_list:
            if not self.__configuration.will_load_all:
                plugin_config = self.__find_plugin_config(plugin)
                if plugin_config == None or not plugin_config['is_enabled']:
                    continue

            loaded_plugin = __import__(plugin)
            loaded_plugins.append({'name': plugin, 'object': loaded_plugin})

        return loaded_plugins

    def execute_plugin_function(self, plugin, function_name='main', args=None):
        return self.__execute_function(plugin['object'], function_name, args)

    def __execute_function(self, plugin, function_name, args=None):
        try:
            if args == None:
                return getattr(plugin, function_name)()
            else:
                return getattr(plugin, function_name)(*args)

        except (AttributeError,) as err:
            if type(err) == AttributeError:
                raise FunctionNotFoundError() from None
            else:
                raise

    def __find_plugin_config(self, plugin_name):
        for plugin_config in self.__configuration.plugins:
            if plugin_config.name == plugin_name:
                return plugin_config

        return None

    # def __verify_plugin_ownership(self, plugin_path):
    #     file_owner_id = pwd.getpwuid(os.stat(plugin_path, follow_symlinks=False).st_uid).pw_uid
    #     file_owner_username = pwd.getpwuid(os.getuid()).pw_name

    #     if self.__is_sudo():
    #         return str(file_owner_id) == os.environ['SUDO_UID']
    #     else:
    #         return file_owner_username == os.environ['USERNAME']

    def __is_sudo(self):
        try:
            os.environ['SUDO_UID']
            return True
        except:
            return False
