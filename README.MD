# PlugyPy
PlugyPy is a lightweight Python plugin system. It allows executing Python in the form of plugins during program's runtime.

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

Creating a plugin manager object
```python
plugin_manager = plugypy.PluginManager('/path/to/plugins/directory', 'path/to/plugins/configuration/file.json')
```

Importing plugins:
```python
plugins_list = plugin_manager.import_plugins()
```

Getting plugin information:
```python
plugin_name = plugins_list[0]['name']
plugin_executable_object = plugins_list[0]['plugin']
```

Executing plugin with no parameters:
```python
    plugin_result = plugin_manager(plugins_list[0])
    
    if plugin_result == None:
        print('The plugin returned no result')
    else:
        print('The plugin returned: {}'.format(result))
```

Executing plugin with parameters:
```python
    arguments_tuple = ('arg1', 'arg2', 'arg3')
    plugin_result = plugin_manager(plugins_list[0], args=arguments_tuple)
    
    if plugin_result == None:
        print('The plugin returned no result')
    else:
        print('The plugin returned: {}'.format(result))
```
## Writing a configuration file
The configuration (or config) file is a json file that contains a few important bits of information by which the plugin manager knows what
to do with a given plugin.
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

Where `name` is the name of the plugin file without the `.py` file extension, `main_function` is the function that is being call,
and `enabled` is the boolean variable that indicates if the file will be executed (when `true`) or not (when `false`).