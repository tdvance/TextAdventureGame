from player import Player
from room import Room
from dictionary import Dictionary

class Game:
    def __init__(self):
        self._dictionary = Dictionary()
        initial_room = self.setup_rooms()
        self._player = Player(initial_room)
        self.setup_items()
        self.setup_objects()

    @property
    def player(self):
        return self._player

    def restart_game(self):
        """

        :param self:
        """
        self.setup_rooms()
        self.setup_items()
        self.setup_objects()
        self._player.restart()


    def setup_rooms(self):
        """

        :return:
        """
        r1 = Room('rooftop', 'You are on top of a roof')
        r2 = Room('street', 'You are on a street', 'a street')
        r3 = Room('apartment', 'You are in an apartment', 'an apartment')
        r4 = Room('theater', 'You are outside a theater', 'a theater')

        r1.connect('street', 'down')
        r2.connect_two_way('apartment', 'up')
        r2.connect_two_way('theater', 'south')

        return 'rooftop'

    def setup_items(self):
        """

        """
        pass

    def setup_objects(self):
        """

        """
        pass

    def print_state(self):
        print(self.player.room.description)
        for direction, room in self.player.room.connections().items():
            if room.far_description is not None:
                print("%s is %s" % (direction, room.far_description))

if __name__ == '__main__':
    game = Game()
    game.restart_game()
    game.print_state()