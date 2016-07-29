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
        self._indirect_objects = set()  # set of (Preposition, Noun)

    def set_object(self, item):
        self._object = GameObject.get(item)

    def get_object(self):
        return self._object

    def has_object(self):
        return self._object is not None

    def get_indirect_object(self, item):
        item = GameObject.get(item)
        for (p, i) in self._indirect_objects:
            if i == item:
                return i
        return None

    def get_preposition(self, item):
        item = GameObject.get(item)
        for (p, i) in self._indirect_objects:
            if i == item:
                return p
        return None

    def has_indirect_object(self, item):
        item = GameObject.get(item)
        for (p, i) in self._indirect_objects:
            if i == item:
                return True
        return False

    def num_indirect_objects(self):
        return len(self._indirect_objects)

    def iter_indirect_objects(self):
        return iter(self._indirect_objects)

    def add_indirect_object(self, preposition, item):
        item = GameObject.get(item)
        preposition = GameObject.get(preposition)
        self._indirect_objects.add((preposition, item))

    def remove_indirect_object(self, item):
        item = GameObject.get(item)
        for (p, i) in self._indirect_objects:
            if i == item:
                self._indirect_objects.remove((p, i))
                break

    def run(self):
        pass
