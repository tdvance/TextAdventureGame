import resources
from input_parser import Parser
from player import Player
from user_interface import UserInterface
from world import World


class Game:
    def quit(self):
        self._user_interface.print("Bye!")
        exit()

    def __init__(self):
        self._world = World()
        directions = resources.load_directions()
        resources.load_rooms(self._world, directions)
        self._player = Player(self._world.starting_room, directions)
        commands = resources.load_commands(self)
        self._user_interface = UserInterface(commands)

        aliases = resources.load_aliases()
        errors = resources.load_errors()
        parser = Parser(directions, commands, aliases, errors)

        while True:
            self._user_interface.describe_room(self._player.room)
            (cmd, *args) = parser.get_input()
            result = cmd(*args)
            if result:
                result.show()

    @property
    def world(self):
        return self._world

    @property
    def user_interface(self):
        return self._user_interface

    @property
    def player(self):
        return self._player


game = Game()
