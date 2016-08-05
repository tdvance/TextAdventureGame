class Action:
    def __init__(self, name, obj, method, help_text):
        assert hasattr(method, '__call__')
        self._name = str(name)
        self._obj = obj
        self._method = method
        self._help = str(help_text)

    @property
    def name(self):
        return self._name

    @property
    def help(self):
        return self._help

    def __call__(self, *args):
        return self._method.__call__(*args)

    def __str__(self):
        return self.name
