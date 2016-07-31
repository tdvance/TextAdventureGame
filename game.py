import csv
from collections import namedtuple
import random
import sys

from resources import Resources

class Game:
    def __init__(self):
        self._starting_room = None
        self._room = None
        self._time = 0.0
        self._resources = Resources()
        self.load_game()
        self._debug = False

    def load_game(self):
        self._starting_room = self._resources.load_resource('Room')
        self._resources.load_resource('Direction')
        self._resources.load_resource('Synonym')

    def start_game(self):
        self._room = self._starting_room
        self._time = 0.0
        while self.tick():
            pass
        self.output_sentence("Game Over")

    def tick(self):
        self.show_room()
        l = self.get_input()
        result = self.process_input(l)
        self._time += 1
        return result

    def output_sentence(self, fmt, *args):
        x = fmt % args
        x = x[0].upper() + x[1:] + '.'
        print(x)

    def debug(self, fmt, *args):
        if self._debug:
            print("Debug: ", end='')
            print(fmt % args)

    def show_room(self, brief=False):
        self.debug("%s", self._room)
        r = self._resources.get(self._room, 'Room')
        self.output_sentence("%s", r.Description)
        if brief:
            return
        #TODO fix
        for d in r.obj:
            direction = self.resources.get(d, 'Direction')
            w = r.obj[d]
            where = self.resources.find(w, 'Room')
            self.debug("d=%s:direction=%s, w=%s:where=%s", d, direction, w, where)
            self.output_sentence("%s is %s", random.choice(direction.obj.texts), where.short_description)

    def get_input(self):
        s = input('> ')
        return s.split()

    def process_input(self, l):
        # self.output_sentence("cmd = %r", l)
        if not l:
            return
        cmd = l[0]
        if cmd == 'quit':
            return False
        if cmd == 'go':
            return self.go(*l[1:])
        if len(l) == 1 and self.resources.find(cmd, 'Direction'):
            return self.go(cmd)
        self.output_sentence("I don't understand")
        return "I don\'t understand"

    def go(self, *args):
        if not args:
            self.output_sentence("Go where?")
            return 'redo'
        where = self.resources.find(args[0], 'Direction')
        if where is None:
            self.output_sentence("I don't understand %r", args[0])
            return 'redo'
        r = self.resources.find(self._room, 'Room')
        if where.name not in r.obj:
            self.output_sentence("There is nothing to see %s", random.choice(where.obj.texts))
            return 'redo'
        next_room = r.obj[where.name]
        self._room = next_room
        return 'ok'


if __name__ == '__main__':
    game = Game()
    # game._registry.dump()
    game.start_game()
