import resources
from input_parser import Parser
from player import Player
from world import World


class Game:
    def quit(self):
        exit()

    def __init__(self):
        world = World()
        directions = resources.load_directions()
        resources.load_rooms(world, directions)
        player = Player(world.starting_room, directions)
        actions = resources.load_actions(player=player, world=world, game=self)
        aliases = resources.load_aliases()
        errors = resources.load_errors()
        parser = Parser(directions, actions, aliases, errors)

        while True:
            player.room.show()
            player.room.show_connecting()
            (cmd, *args) = parser.get_input()
            result = cmd(*args)
            if result:
                result.show()


game = Game()
