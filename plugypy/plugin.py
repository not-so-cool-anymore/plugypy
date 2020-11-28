class Plugin(object):
    name: str
    is_enabled: bool

    def __init__(self, name: str, is_enabled: bool):
        self.name = name
        self.is_enabled = is_enabled
