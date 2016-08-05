from room import Room


class World:
    def __init__(self):
        self._rooms = dict()
        self._starting_room = None

    def __setitem__(self, name, room):
        assert isinstance(room, Room)
        assert room not in self
        assert str(name).lower() == str(room.name).lower()
        self._rooms[str(name).lower()] = room

    def __contains__(self, name):
        return str(name).lower() in self._rooms

    def __getitem__(self, name):
        return self._rooms[str(name).lower()]

    def __iter__(self):
        return iter(self._rooms)

    def __delitem__(self, name):
        del self._rooms[str(name).lower()]

    def __len__(self):
        return len(self._rooms)

    def __str__(self):
        return 'A world with %d rooms' % len(self)

    def set_starting_room(self, room):
        assert isinstance(room, Room)
        self._starting_room = room

    @property
    def starting_room(self):
        return self._starting_room

    def dump(self):
        for room in self._rooms.values():
            print(room.name + ' -> ')
            for direction, r in room._connections.items():
                print('   ' + direction.name + ': ' + r.target.name)
