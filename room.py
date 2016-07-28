from globals import reverse_directions

class Room:
    _registry = dict()

    @classmethod
    def get(cls, name):
        if isinstance(name, cls):
            return name
        return cls._registry[name]

    def __init__(self, name,
                 description="You are in a maze of twisty passages, all alike.",
                 far_description=None):
        assert isinstance(name, str)
        assert isinstance(description, str)
        assert far_description is None or isinstance(far_description, str)
        Room._registry[name] = self
        self._description = description
        self._far_description = far_description
        self._name = name
        self._connects_to = dict()  # direction:room

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def far_description(self):
        return self._far_description

    def connect(self, room, direction):
        self._connects_to[direction] = Room.get(room)

    def connect_two_way(self, room, direction, reverse_direction=None):
        if reverse_direction is None:
            reverse_direction = reverse_directions[direction]
        self.connect(room, direction)
        other = Room.get(room)
        other.connect(self.name, reverse_direction)

    def connections(self):
        return self._connects_to

if __name__ == '__main__':
    x = Room("ARoom")
    y = Room("AnotherRoom")
    for room in Room._registry.values():
        print(room)

    x.connect_two_way('AnotherRoom', 'south')
