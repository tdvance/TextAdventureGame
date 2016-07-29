from game_object import GameObject


class Action(GameObject):
    """
    An action is something that an actor (player, enemy) can do.  It can have an object (a noun),
    and multiple indirect objects (selected with prepositions).
    """

    def __init__(self, name, desc=None, brief_desc=None):
        GameObject.__init__(self, self.__class__, name, desc, brief_desc)

    def set_object(self, item):
        pass

    def get_object(self):
        pass

    def has_object(self):
        pass

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
