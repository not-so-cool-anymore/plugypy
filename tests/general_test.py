import os
import plugypy
import unittest

current_folder = os.path.dirname(os.path.realpath(__file__))

arguments = [
    ('param',),
    (),
    (1,2)
]

class GeneralTest(unittest.TestCase):
    def test_plugins_configuration_deserialization(self):
        deserializer = plugypy.ConfigurationDeserializer(current_folder + '/plugins/config.json')
        plugins_configuraiton = deserializer.deserialize_config()

    def test_plugin_manager_instantiation(self):
        deserializer = plugypy.ConfigurationDeserializer(current_folder + '/plugins/config.json')
        plugins_configuraiton = deserializer.deserialize_config()
        
        plugin_manager = plugypy.PluginManager(
            current_folder + '/plugins', 
            plugins_configuraiton, 
            True
        )
        
        self.assertIsInstance(plugin_manager, plugypy.PluginManager)

    def test_plugins_discovery(self):
        deserializer = plugypy.ConfigurationDeserializer(current_folder + '/plugins/config.json')
        plugins_configuraiton = deserializer.deserialize_config()
        
        plugin_manager = plugypy.PluginManager(
            current_folder + '/plugins', 
            plugins_configuraiton, 
            True
        )

        discovered_plugins = plugin_manager.discover_plugins()
        self.assertIsInstance(discovered_plugins, list)

    def test_plugins_import(self):
        deserializer = plugypy.ConfigurationDeserializer(current_folder + '/plugins/config.json')
        plugins_configuraiton = deserializer.deserialize_config()
        
        plugin_manager = plugypy.PluginManager(
            current_folder + '/plugins', 
            plugins_configuraiton, 
            True
        )

        discovered_plugins = plugin_manager.discover_plugins()
        imported_plugins = plugin_manager.import_plugins(discovered_plugins)
        self.assertIsInstance(imported_plugins, list)


    def test_print_argument(self):
        deserializer = plugypy.ConfigurationDeserializer(current_folder + '/plugins/config.json')
        plugins_configuraiton = deserializer.deserialize_config()
        
        plugin_manager = plugypy.PluginManager(
            current_folder + '/plugins', 
            plugins_configuraiton, 
            True
        )

        discovered_plugins = plugin_manager.discover_plugins()
        imported_plugins = plugin_manager.import_plugins(discovered_plugins)

        result = plugin_manager.execute_plugin_function(
            imported_plugins[0],
            function_name = 'print_argument',
            args = arguments[0]
            )

        self.assertIsNone(result)

    def test_print_message(self):
        deserializer = plugypy.ConfigurationDeserializer(current_folder + '/plugins/config.json')
        plugins_configuraiton = deserializer.deserialize_config()
        
        plugin_manager = plugypy.PluginManager(
            current_folder + '/plugins', 
            plugins_configuraiton, 
            True
        )

        discovered_plugins = plugin_manager.discover_plugins()
        imported_plugins = plugin_manager.import_plugins(discovered_plugins)
        
        result = plugin_manager.execute_plugin_function(
            imported_plugins[1],
            function_name = 'print_message',
            args = arguments[1]
        )

        self.assertIsNone(result)
    
    def test_sum(self):
        deserializer = plugypy.ConfigurationDeserializer(current_folder + '/plugins/config.json')
        plugins_configuraiton = deserializer.deserialize_config()
        
        plugin_manager = plugypy.PluginManager(
            current_folder + '/plugins', 
            plugins_configuraiton, 
            True
        )

        discovered_plugins = plugin_manager.discover_plugins()
        imported_plugins = plugin_manager.import_plugins(discovered_plugins)

        result = plugin_manager.execute_plugin_function(
            imported_plugins[2],
            function_name = 'sum_arguments',
            args = arguments[2]
            )

        self.assertEqual(result, sum(arguments[2]))

if __name__ == '__main__':
    unittest.main()
