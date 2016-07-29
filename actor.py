from item import Item


class Actor(Item):
    def __init__(self, name, desc=None, brief_desc=None):
        Item.__init__(self, name, desc, brief_desc)

    @property
    def status(self):
        pass

    def do_action(self, action, *pargs, **kwargs):
        pass
