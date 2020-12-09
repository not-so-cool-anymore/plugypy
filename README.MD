# PlugyPy
![plugypy](https://socialify.git.ci/not-so-cool-anymore/plugypy/image?description=1&descriptionEditable=PlugyPy%20is%20a%20lightweight%20Python%20plugin%20system.%20It%20allows%20executing%20Python%20in%20the%20form%20of%20plugins%20during%20program%27s%20runtime.&font=KoHo&language=1&owner=1&pattern=Circuit%20Board&stargazers=1&theme=Dark)

## Installation
You can install the plugin system from PyPi with:

```
pip install PlugyPy
```

Or locally by cloning the repository:

```
git clone https://github.com/not-so-cool-anymore/plugypy.git
```
and then running the setup file in the main directory with:
```
pip install .
```

## Writing a configuration file
A PlugyPy configuration (or config) file is a JSON file that contains a deserialized representation of a PlugyPy `Configuration` object.
The `Configuration` object consists of a boolean named `will_load_all` and a list named `plugins`.
`plugins` is a list of PlugyPy `Plugin` objects  `will_load_all` determines whether all of the plugins in the plugins directory will be loaded or only the enabled ones.

An example of a config file is:
```json
{
    "will_load_all": true,
    "plugins": [
        {
            "name": "example_plugin_name_0",
            "is_enabled": true
        },
        {
            "name": "example_plugin_name_1",
            "is_enabled": false
        },
        {
            "name": "example_plugin_name_2",
            "is_enabled": true
        }
    ] 
}
```

Where `name` is the name of the plugin file without the `.py` file extension, and `enabled` is the boolean variable that indicates whether a plugin will be loaded (when `true`) or not (when `false`).

## Usage
Importing the plugin system:
```python
import plugypy
```


Deserializing JSON configuration file into a `Configuration` object.
```python
configuration_deserializer = ConfigurationDeserializer('/path/to/configuration/file')
configuration = configuration_deserializer.deserialize_config()
```


Creating a plugin manager object:
```python
plugin_manager = plugypy.PluginManager('/path/to/plugins/directory', configuration)
```
The plugin manager object has one extra feature - plugin ownership verification. This feature ensures that the plugin that is being executed
belongs to the current user (or if `sudo` is used to run the program - the `sudo` caller).
This feature can be activated via parsing one extra argument - `will_verify_ownership=True`, which is set to `False` by default when not passed.


Discovering plugins:
```python
discovered_plugins = plugin_manager.discover_plugins()
```
`discover_plugins` is a list of all the plugins in a given plugins directory.


Importing plugins:
```python
plugins_list = plugin_manager.import_plugins(discovered_plugins)
```
`plugins_list` is a list of map objects that has a `name` key and an `object` value of the imported executable Python module (plugin executable).


Importing a singe plugin by file name:
```python
single_plugin = plugin_manager.import_plugin('PLUGIN_FILENAME_WITHOUT_PY_EXTENSION')
```
In this case, the plugin will be imported no matter if a configuration for it exists. This importing method is developed for edge cases in which the imported plugin will be
executed only once.


Getting a plugin's information:
```python
plugin_name = plugins_list[n]['name']
plugin_executable_object = plugins_list[n]['object']
```
`n` is an index of a plugin.


Executing a plugin's function with no parameters:
```python
plugin = plugins_list[n]
plugin_result = plugin_manager.execute_plugin_function(plugin, 'function_name')

if plugin_result == None:
    print('The plugin returned no result')
else:
    print('The plugin returned: {}'.format(result))
```
`n` is an index of a plugin.


Executing a plugin's function with parameters:
```python
plugin = plugins_list[n]

arguments_tuple = ('arg1', 'arg2', 'arg3')
plugin_result = plugin_manager.execute_plugin_function(plugin, 'function_name', args=arguments_tuple)

if plugin_result == None:
    print('The plugin returned no result')
else:
    print('The plugin returned: {}'.format(result))
```
`n` is an index of a plugin.

`args` must be a tuple of argument/s.
