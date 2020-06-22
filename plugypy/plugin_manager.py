import os
import pwd
import sys
import json
from .plugypy_errors import MainFunctionNotFoundError

class PluginManager():
    def __init__(self, plugins_folder_location, config_file_location, will_verify_ownership=False):
        self.__plugins_folder_location = plugins_folder_location
        self.__config_file_location = config_file_location
        self.__will_verify_plugins_ownership = will_verify_ownership

        self.__load__plugins_configuration()

    def import_plugins(self):
        plugins = list()
        plugins_directory_content = os.listdir(self.__plugins_folder_location)
    
        sys.path.insert(1, self.__plugins_folder_location)

        for content in plugins_directory_content:
            content_location = self.__plugins_folder_location + '/' + content

            if (os.path.isdir(content_location) or content == '__init__.py' or 
                    content.endswith('.pyc') or content.endswith('.json')):
                continue
            
            if self.__will_verify_plugins_ownership and not self.__verify_plugin_ownership(content_location):
                print('nope')
                continue

            plugin_name = content.replace('.py', '')
            
            if self.__find_plugin_config(plugin_name) == None:
                continue

            plugin = __import__(plugin_name)
            plugins.append({'name' : plugin_name, 'plugin' : plugin})

        return plugins

    def import_plugin(self, name):
        plugins_directory_content = os.listdir(self.__plugins_folder_location)
    
        sys.path.insert(1, self.__plugins_folder_location)

        for content in plugins_directory_content:
            content_location = self.__plugins_folder_location + '/' + content

            if (os.path.isdir(content_location) or content == '__init__.py' or 
                    content.endswith('.pyc') or content.endswith('.json')):
                continue
            
            if self.__will_verify_plugins_ownership and not self.__verify_plugin_ownership(content_location):
                continue

            plugin_name = content.replace('.py', '')
            
            if plugin_name == name:
                plugin = __import__(plugin_name)
                return {'name' : plugin_name, 'plugin' : plugin}
        
        return None

    def execute_plugin(self, plugin, args=None, is_forced=False):
        result = None
        plugin_name = plugin['name']
        plugin_config = self.__find_plugin_config(plugin_name)

        if is_forced:
            result = self.__execute_function(plugin['plugin'], 'main', args)
        else:
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

        except (AttributeError,) as err:
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
    
    def __verify_plugin_ownership(self, plugin_path):
        file_owner_id = pwd.getpwuid(os.stat(plugin_path, follow_symlinks=False).st_uid).pw_uid
        file_owner_username = pwd.getpwuid(os.getuid()).pw_name

        if self.__is_sudo():
            return str(file_owner_id) == os.environ['SUDO_UID']
        else:
            return file_owner_username == os.environ['USERNAME']

    def __is_sudo(self):
        try:
            os.environ['SUDO_UID']
            return True
        except:
            return False