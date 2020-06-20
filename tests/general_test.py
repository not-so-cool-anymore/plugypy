import os
import plugypy
import unittest

current_folder = os.path.dirname(os.path.realpath(__file__))

params = [
    (),
    ('param',),
    (1,2)
]

class GeneralTest(unittest.TestCase):
    def test_plugin_manager_instantiation(self):
        self.__class__.plugin_manager = plugypy.PluginManager(current_folder + '/plugins', current_folder + '/plugins/config.json')
        self.assertIsInstance(self.plugin_manager, plugypy.PluginManager)

    def test_plugins_import(self):
        self.assertIsInstance(self.__class__.plugin_manager.import_plugins(), list)

    def test_print_message(self):
        plugins = self.__class__.plugin_manager.import_plugins()
        self.assertIsNone(self.__class__.plugin_manager.execute_plugin(plugins[0], params[0]))
    
    def test_print_argument(self):
        plugins = self.__class__.plugin_manager.import_plugins()
        self.assertIsNone(self.__class__.plugin_manager.execute_plugin(plugins[1], params[1]))
    
    def test_sum(self):
        plugins = self.__class__.plugin_manager.import_plugins()
        self.assertEqual(self.__class__.plugin_manager.execute_plugin(plugins[2], params[2]), sum(params[2]))

if __name__ == '__main__':
    unittest.main()