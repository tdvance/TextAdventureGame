from room import Room


class Player:
    def __init__(self, room, directions):
        assert isinstance(room, Room)
        self._room = room
        self._directions = directions

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, value):
        assert isinstance(value, Room)
        self._room = value

    def go(self, where):
        self._room = self._room.get_connecting(self._directions[where.lower()])

    def __str__(self):
        return "Player in room %s" % self._room
