from game_object import GameObject


class Noun(GameObject):
    """
    A noun is a game object representing something in the game: an actor, item, room, the game itself, etc.

    This is in contrast to an action (a verb) or a preposition (a syntactic elemnet for the console user interface).

    Usually accessed via subclasses rather than used directly.
    """

    def __init__(self, cls, name, desc=None, brief_desc=None):
        GameObject.__init__(self, cls, name, desc, brief_desc)
