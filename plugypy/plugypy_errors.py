class FunctionNotFoundError(Exception):
    def __init__(self):
        super().__init__('Provided function was not found in the plugin file.')

class InvalidConfigurationFile(Exception):
    def __init__(self):
        super().__init__('Invalid configuration file. Configuration cannot be deserialized properly.')