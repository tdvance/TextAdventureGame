import csv
from collections import namedtuple
import random
import sys

import resources


class Game:
    def __init__(self):
        self._starting_room = None
        self._room = None
        self._time = 0.0
        self._resources = resources.Resources()
        self.load_game()
        self._debug = False

    def load_game(self):
        self._starting_room = self._resources.load_resource('Room')
        self._resources.load_resource('Direction')
        self._resources.load_resource('Command')
        self._resources.load_resource('Synonym')

    def start_game(self):
        self._room = self._starting_room
        self._time = 0.0
        while self.tick():
            pass
        self.output_sentence("Game Over")

    # Main Loop
    def tick(self):
        self.show_room()
        l = self.get_input()
        result = self.process_input(l)
        self._time += 1
        return result

    def output_sentence(self, fmt, *args):
        x = fmt % args
        if x.endswith('.'):
            x = x[0].upper() + x[1:]
        else:
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
        i = 3
        while i < len(r) and r[i]:
            d = r[i]
            w = r[i + 1]
            i += 2
            direction = self._resources.get(d, 'Direction')
            where = self._resources.get(w, 'Room')
            l = 2
            while direction[l] and l < len(direction):
                l += 1
            self.debug("d=%s:direction=%s, w=%s:where=%s", d, direction, w, where)
            self.output_sentence("%s is %s", random.choice(direction[2:l]), where.ShortDescription)

    def get_input(self):
        s = input('> ')
        return s.lower().split()

    def process_input(self, l):
        if not l:
            return
        cmd = l[0]
        if len(l) == 1 and self._resources.has(cmd, 'Direction'):
            return self.go(cmd)
        cmd, category = self._resources.normalize(cmd, 'Command')
        if cmd == 'help':
            return self.help(*l[1:])
        if cmd == 'quit':
            return False
        if cmd == 'go':
            return self.go(*l[1:])

        self.output_sentence("I don't understand")
        return "I don't understand"

    def help(self, *args):
        if args:
            x = args[0].lower()
            if self._resources.has(x, 'Command'):
                x = self._resources.get(x, 'Command')
                self.output_sentence("%s", x.Description)
                return 'ok'
            if self._resources.has(x, 'Direction'):
                x = self._resources.get(x, 'Direction').Name
                self.output_sentence("Go %s", x)
                return 'ok'
            self.output_sentence("I don't understand")
            return "I don't understand"
        self.output_sentence(
            "A sampling of commands: go, get, drop, quit, save, load, look, north, south, up, down, and so on.  Help <cmd> for more information")
        return 'ok'

    def go(self, *args):
        if not args:
            self.output_sentence("Go where?")
            return 'redo'
        where = self._resources.get(args[0], 'Direction')
        if where is None:
            self.output_sentence("I don't understand %r", args[0])
            return 'redo'
        r = self._resources.get(self._room, 'Room')
        for i in range(3, len(r), 2):
            if r[i].lower() == where.Name.lower():
                next_room = r[i + 1]
                self._room = next_room
                return 'ok'
        l = 2
        while where[l] and l < len(where):
            l += 1
        self.output_sentence("There is nothing to see %s", random.choice(where[2:l]))
        return 'redo'


if __name__ == '__main__':
    game = Game()
    game.start_game()
