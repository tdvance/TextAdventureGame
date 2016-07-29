from action import Action
from actor import Actor
from dictionary import Dictionary
from direction import Direction
from enemy import Enemy
from game_object import GameObject
from item import Item
from noun import Noun
from player import Player
from preposition import Preposition
from room import Room


class Game(Noun):
    """
    The main game, managing the game loop, containers for various game elements, etc.
    """
    def __init__(self, game='Game', desc=None, brief_desc=None):
        Noun.__init__(self, self.__class__, game, desc, brief_desc)

    @property
    def player(self):
        pass

    @property
    def dictionary(self):
        pass

    def __getitem__(self, item):
        pass

    def __contains__(self, item):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def add_item(self, item):
        pass

    def __delitem__(self, item):
        pass

    def get_room(self, room):
        pass

    def has_room(self, room):
        pass

    def num_rooms(self):
        pass

    def iter_rooms(self):
        pass

    def add_room(self, room):
        pass

    def remove_room(self, room):
        pass


if __name__ == '__main__':
    print("Running main.")
    game = Game()
    print("Game(%s) = %r " % (game, game))
