from game_object import GameObject


class Preposition(GameObject):
    """
    A preposition connects actions to nouns (e.g X does something to or with or on the Y),
    or nouns to other nouns (e.g. X is inside or on top of or with the Y)
    """

    def __init__(self, name, desc=None, brief_desc=None):
        GameObject.__init__(self, self.__class__, name, desc, brief_desc)
