from noun import Noun


class Room(Noun):
    """
    A room is a noun that can contain (via a preposition) items or be connected to other rooms via a direction.
    """

    def __init__(self, name, desc=None, brief_desc=None):
        Noun.__init__(self, self.__class__, name, desc, brief_desc)

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

    def get_room(self, direction):
        pass

    def has_room(self, direction):
        pass

    def num_rooms(self):
        pass

    def iter_rooms(self):
        pass

    def add_room(self, direction, room):
        pass

    def remove_room(self, direction):
        pass
