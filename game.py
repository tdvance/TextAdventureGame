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

    def read_command(self):
        l = input("> ").split()
        return [ self._dictionary.lookup(x) for x in l]

    def tick(self):
        self.print_state()
        cmd = self.read_command()
        if cmd:
            self.exec(cmd)

    def exec(self, cmd):
        if str(cmd[0]) == 'go':
            if len(cmd)==1:
                print("Go where?")
            elif len(cmd) > 2 or cmd[1] is None:
                print("I don't understand.")
            elif 'direction' not in cmd[1]._categories:
                print("%s is not a direction" % str(cmd[1]))
            else:
                self.player.go(str(cmd[1]))



if __name__ == '__main__':
    game = Game()
    for i in range(5):
        game.tick()