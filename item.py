from noun import Noun
from game_object import GameObject
from preposition import Preposition


class Item(Noun):
    """
    An item is a noun than can be spawned or deleted (not the same as killed, which means setting health to 0),
    and can contain or be contained in other items (via a preposition)
    """

    def __init__(self, name, desc=None, brief_desc=None):
        Noun.__init__(self, self.__class__, name, desc, brief_desc)
        self._items = set()
        self._contained_in = None
        self._preposition = None

    def __getitem__(self, item):
        pass

    def get_preposition(self, item):
        pass

    def __contains__(self, item):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def add_item(self, item, preposition):
        pass

    def __delitem__(self, item):
        pass

    def spawn(self, prepostion, where):
        self._contained_in = GameObject.get(where, [Room, Player, Enemy, Item, Actor])
        self._preposition = GameObject.get(prepostion, [Preposition])
        self._contained_in.add_item(self, self._preposition)
        pass

    def delete(self):
        del self._contained_in[self]
        self._contained_in = None
        self._preposition = None
        pass
