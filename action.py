from game_object import GameObject
from noun import Noun
from preposition import Preposition


class Action(GameObject):
    """
    An action is something that an actor (player, enemy) can do.  It can have an object (a noun),
    and multiple indirect objects (selected with prepositions).

    a = Action("anAction") -> creates an action
    """

    def __init__(self, name, desc=None, brief_desc=None):
        GameObject.__init__(self, self.__class__, name, desc, brief_desc)
        self._object = None
        self._indirect_objects = []  # list of (Preposition, Noun)

    def set_object(self, item):
        self._object = GameObject.get(item)

    def get_object(self):
        return self._object

    def has_object(self):
        return self._object is not None

    def get_indirect_object(self, item):
        pass

    def get_preposition(self, item):
        pass

    def has_indirect_object(self, item):
        pass

    def num_indirect_objects(self):
        pass

    def iter_indirect_objects(self):
        pass

    def add_indirect_object(self, preposition, item):
        pass

    def remove_indirect_object(self, item):
        pass

    def run(self):
        pass
