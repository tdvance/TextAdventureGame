from item import Item


class Actor(Item):
    """
    An actor is an item that can perform an action, possibly on items via prepositions.
    """

    def __init__(self, name, desc=None, brief_desc=None):
        Item.__init__(self, name, desc, brief_desc)

    def do_action(self, action, *pargs, **kwargs):
        pass
