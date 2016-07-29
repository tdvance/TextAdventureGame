from game_object import GameObject


class Noun(GameObject):
    def __init__(self, cls, name, desc=None, brief_desc=None):
        GameObject.__init__(self, cls, name, desc, brief_desc)
