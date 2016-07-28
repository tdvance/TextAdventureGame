from room import Room

# a singleton class
class Player:
    _player = None
    _initial_room = None

    def __init__(self, initial_room):
        assert Player._player is None
        Player._player = self
        Player._initial_room = Room.get(initial_room)
        self._room = None
        self._inventory = None
        self._health = None
        self.restart()


    def restart(self):
        self._room = Player._initial_room
        self._inventory = set()
        self._health = 1.0  # relative health--from 0.0 to 1.0

    @property
    def room(self):
        """

        :return:
        """
        return self._room

    @property
    def health(self):
        """

        :return:
        """
        return self._health

    def take(self, item):
        """

        :param item:
        """
        pass

    def drop(self, item):
        """

        :param item:
        """
        pass

    def go(self, direction):#TODO handle directions that do not go anywhere
        self._room = self.room._connects_to[direction]

