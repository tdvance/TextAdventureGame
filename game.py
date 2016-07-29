from itertools import chain

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

    def __init__(self, game='Game', player_name="Player", desc=None, brief_desc=None):
        Noun.__init__(self, self.__class__, game, desc, brief_desc)
        self._dictionary = Dictionary()
        self._player = Player(str(player_name))
        self._registry = GameObject._registry

    @property
    def player(self):
        return self._player

    @property
    def dictionary(self):
        return self._dictionary

    def __getitem__(self, item):
        return self._registry.find(item, {Item, Actor, Player, Enemy})

    def __contains__(self, item):
        return self[item] is not None

    def __len__(self):
        return (self._registry.count(Item) + self._registry.count(Actor)
                + self._registry.count(Player) + self._registry.count(Enemy))

    def __iter__(self):
        return chain(self._registry.iter(Item), self._registry.iter(Actor),
                     self._registry.iter(Player), self._registry.iter(Enemy))

    def get_room(self, room):
        return self._registry.get(room, Room)

    def has_room(self, room):
        return self._registry.get(room, Room) is not None

    def num_rooms(self):
        return self._registry.count(Room)

    def iter_rooms(self):
        return self._registry.iter(Room)


if __name__ == '__main__':
    print("Running main.")
    game = Game(game='A Game', player_name='A Player')
    print("Game(%s) = %r " % (game, game))
