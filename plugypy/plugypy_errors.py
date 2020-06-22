class MainFunctionNotFoundError(Exception):
    def __init__(self):
        super().__init__('Provided main function was not found in the plugin file.')