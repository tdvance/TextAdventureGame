from registry import Registry
from globals import reverse_directions


class Room:
    def __init__(self, name,
                 description="You are in a maze of twisty passages, all alike.",
                 far_description=None):
        Registry.add_room(name, self)
        self._description = description
        self._far_description = far_description
        self._name = name
        self._connects_to = dict()  # direction_string:room_name

    def __str__(self):
        return self.name + ": " + self.description

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def far_description(self):
        return self._far_description

    def connect(self, room_name, direction):
        self._connects_to[direction] = room_name
        return Registry.contains(room_name)

    def connect_two_way(self, room_name, direction, reverse_direction=None):
        if reverse_direction is None:
            reverse_direction = reverse_directions[direction]
        if self.connect(room_name, direction):
            other = Registry.get_room(room_name)
            other.connect(self.name, reverse_direction)
        else:
            Registry.error("Room %s does not exist", room_name)


if __name__ == '__main__':
    x = Room("ARoom")
    y = Room("AnotherRoom")
    for room in Registry.all_rooms.values():
        print(room)

    x.connect_two_way('AnotherRoom', 'south')
