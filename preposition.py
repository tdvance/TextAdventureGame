from game_object import GameObject


class Preposition(GameObject):
    def __init__(self, name, desc=None, brief_desc=None):
        GameObject.__init__(self, self.__class__, name, desc, brief_desc)