import os
import pwd
import sys
import json
from . import MainFunctionNotFoundError

class PluginManager():
    def __init__(self, plugins_folder_location, config_file_location):
        self.__plugins_folder_location = plugins_folder_location
        self.__config_file_location = config_file_location

        self.__load__plugins_configuration()
        self.__plugins = None

    def import_plugins(self):
        plugins = list()
        plugins_directory_content = os.listdir(self.__plugins_folder_location)
    
        sys.path.insert(1, self.__plugins_folder_location)

        for content in plugins_directory_content:
            content_location = self.__plugins_folder_location + '/' + content

            if os.path.isdir(content_location) or content == '__init__.py' or content.endswith('.pyc'):
                continue
            
            plugin_name = content.replace('.py', '')

            plugin = __import__(plugin_name)
            plugins.append({'name' : plugin_name, 'plugin' : plugin})

        self.__plugins = plugins
        return self.__plugins
            
    def execute_plugin(self, plugin, args=None):
        plugin_name = plugin['name']
        plugin_config = self.__find_plugin_config(plugin_name)
            
        if plugin_config == None or not plugin_config['enabled']:
            return None

        plugin_main_function = plugin_config['main_function']

        result = self.__execute_function(plugin['plugin'], plugin_main_function, args)

        return result

    def __execute_function(self, function_file, function_name, args=None):
        try:
            if args == None:
                return getattr(function_file, function_name)()
            else:
                return getattr(function_file, function_name)(*args)

        except (AttributeError, ) as err:
            if type(err) == AttributeError:
                raise MainFunctionNotFoundError() from None
            else:
                raise


    def __find_plugin_config(self, plugin_name):
        for plugin_config in self.__plugins_configuration:
            if plugin_config['name'] == plugin_name:
                return plugin_config

        return None

    def __load__plugins_configuration(self):
        with open(self.__config_file_location) as config_file:
            self.__plugins_configuration = json.load(config_file)
    
    def __verify_plugin_ownership(self):
        return True
    


#plugin_manager = PluginManager(os.path.dirname(os.path.realpath(__file__)) + '/plugins', '/home/ivan/Downloads/plg_conf.json')

#plugins = plugin_manager.import_plugins()
#plugin_manager.execute_plugin(plugins[0])