from noun import Noun


class Direction(Noun):
    """
    A direction is where a player can go (action) to (indirect object or object), such as west, up, etc.
    """

    def __init__(self, name, desc=None, brief_desc=None):
        Noun.__init__(self, self.__class__, name, desc, brief_desc)
