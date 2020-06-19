import plugypy

plugin_manager = plugypy.PluginManager('/home/ivan/plugins','/home/ivan/plugins/config.json')

plugins_list = plugin_manager.import_plugins()

for plugin in plugins_list:
    plugin_result = plugin_manager.execute_plugin(plugin[0])
    print('Plugin execution returned: {}'.format(plugin_result))

print('All plugins were executed.')