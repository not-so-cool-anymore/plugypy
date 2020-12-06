import os
import plugypy
import unittest

current_folder = os.path.dirname(os.path.realpath(__file__))

arguments = [
    (),
    ('param',),
    (1,2)
]

class GeneralTest(unittest.TestCase):
    def test_plugins_configuration_deserialization(self):
        deserializer = plugypy.ConfigurationDeserializer(current_folder + '/plugins/config.json')
        self.__class__.plugins_configuraiton = deserializer.deserialize_config()

    def test_plugin_manager_instantiation(self):
        print(self.__class__.__dict__)
        self.__class__.plugin_manager = plugypy.PluginManager(
            current_folder + '/plugins', 
            self.__class__.plugins_configuraiton, 
            True
            )
        self.assertIsInstance(self.plugin_manager, plugypy.PluginManager)

    def test_plugins_discovery(self):
        self.__class__.discovered_plugins = self.__class__.plugin_manager.discover_plugins()
        self.assertIsInstance(self.__class__.discovered_plugins)

    def test_plugins_import(self):
        self.__classs__.imported_plugins = self.__class__.plugin_manager.import_plugins(self.__class__.discovered_plugins)
        self.assertIsInstance(self.__classs__.imported_plugins, list)

    def test_print_message(self):
        result = self.__class__.plugin_manager.execute_plugin_function(
            self.__class__.imported_plugins,
            function_name = 'print_message',
            args = arguments[0]
            )

        self.assertIsNone(result)
    
    def test_print_argument(self):
        result = self.__class__.plugin_manager.execute_plugin_function(
            self.__classs__.imported_plugins,
            function_name = 'print_argument',
            args = arguments[1]
            )

        self.assertIsNone(result)
    
    def test_sum(self):
        result = self.__class__.plugin_manager.execute_plugin_function(
            self.__classs__.imported_plugins,
            function_name = 'sum',
            args = arguments[2]
            )

        self.assertEqual(result, sum(arguments[2]))

if __name__ == '__main__':
    unittest.main()
