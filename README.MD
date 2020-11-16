# PlugyPy
![plugypy](https://socialify.git.ci/not-so-cool-anymore/plugypy/image?description=1&font=KoHo&language=1&owner=1&pattern=Circuit%20Board&stargazers=1&theme=Dark)

## Installation
You can install the plugin system from PyPi with:

```
pip install PlugyPy
```

Or locally by cloning the repository:

```
git clone git@github.com:not-so-cool-anymore/plugypy.git
```
and then running the setup file in the main directory with:
```
pip install .
```

## Usage
Importing the plugin system:
```python
import plugypy
``` 

Creating a plugin manager object:
```python
plugin_manager = plugypy.PluginManager('/path/to/plugins/directory', 'path/to/plugins/configuration/file.json')
```
The plugin manager object has one extra feature - plugin ownership verification. This feature ensures that the plugin that is being executed
belongs to the current user (or, if `sudo` is used to run the program - the `sudo` caller).
This feature can be activated via parsing one extra argument - `will_verify_ownership=True`, which is set to `False` by default when not passed.


Importing plugins:
```python
plugins_list = plugin_manager.import_plugins()
```


Importing a singe plugin by file name:
```python
single_plugin = plugin_manager.import_plugin('PLUGIN_FILENAME_WITHOUT_PY_EXTENSION')
```
In this case, the plugin will be imported no matter if a configuration for it exists. This importing method is developed for edge cases in which the imported plugin will be
executed only once.


Getting plugin information:
```python
plugin_name = plugins_list[0]['name']
plugin_executable_object = plugins_list[0]['plugin']
```


Executing plugin with no parameters:
```python
    plugin_result = plugin_manager.execute_plugin(plugins_list[0])
    
    if plugin_result == None:
        print('The plugin returned no result')
    else:
        print('The plugin returned: {}'.format(result))
```


Executing plugin with parameters:
```python
    arguments_tuple = ('arg1', 'arg2', 'arg3')
    plugin_result = plugin_manager.execute_plugin(plugins_list[0], args=arguments_tuple)
    
    if plugin_result == None:
        print('The plugin returned no result')
    else:
        print('The plugin returned: {}'.format(result))
```


Forcefully executing a plugin:
```python
    arguments_tuple = ('arg1', 'arg2', 'arg3')
    plugin_result = plugin_manager.execute_plugin(plugins_list[0], args=arguments_tuple, is_forced=True)
    
    if plugin_result == None:
        print('The plugin returned no result')
    else:
        print('The plugin returned: {}'.format(result))
```
Note that in this case we do not supply main function of the plugin. The PluginManager automatically calls
function named `main` and assumes that it is the main function of the plugin. If no function with that name exists a MainFunctionNotFoundError will be thrown. 

## Writing a configuration file
The configuration (or config) file is a JSON file that contains a few important bits of
information by which the plugin manager knows what to do with a given plugin.

An example for a config file is:
```json
[
        {
        "name" : "demo_plugin_0",
        "main_function" : "main_zero",
        "enabled" : true
        },
        {
        "name" : "demo_plugin_1",
        "main_function" : "main_one",
        "enabled" : false
        },

]
```

Where `name` is the name of the plugin file without the `.py` file extension, `main_function` is the function that is being called,
and `enabled` is the boolean variable that indicates if the file will be executed (when `true`) or not (when `false`).