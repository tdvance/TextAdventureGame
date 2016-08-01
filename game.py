import csv
from collections import namedtuple
from collections import deque
import random
import sys

import resources


class Game:
    def __init__(self, *queue):
        """
        Create and run a new game.

        :param queue: commands to inject into input for testing
        """
        self._starting_room = None
        self._room = None
        self._time = 0.0
        self._resources = resources.Resources()
        self.load_game()
        self._debug = False
        self._test_input_queue = deque()
        for s in queue:
            self._test_input_queue.appendleft(str(s))  # for testing
        self._transcript = []

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

    def output(self, fmt, *args):
        x = fmt % args
        self._transcript.append(x)
        print(x)

    def output_sentence(self, fmt, *args):
        x = fmt % args
        if x.endswith('.'):
            x = x[0].upper() + x[1:]
        else:
            x = x[0].upper() + x[1:] + '.'
        self.output('%s', x)

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
        if self._test_input_queue:
            s = self._test_input_queue.pop()
            print('> %s' % s)
        else:
            s = input('> ')
        self._transcript.append('> %s' % s)
        return s.lower().split()

    def process_input(self, l):
        if not l:
            return 'Enter a command.'
        cmd = l[0]
        if len(l) == 1 and self._resources.has(cmd, 'Direction'):
            return self.go(cmd)
        r = self._resources.get(cmd, 'Command')
        if r is None:
            self.output_sentence("I am not familiar with the command '%s'", cmd)
            return "I don't understand"
        cmd = r.Name
        if cmd == 'Help':
            return self.help(*l[1:])
        if cmd == 'Quit':
            return False
        if cmd == 'Go':
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
    game = Game('d', 'w', 'e', 's', 'go w', 'e', 'n', 'south', 'North', 'nw', 'h nw', 'q')
    game.start_game()
    t = game._transcript
    assert 'top of a roof' in t[0]
    assert 'street below a tall building' in t[3]
    assert 'apartment building' in t[7]
    assert t[10] == t[3]
    assert 'decrepit theater' in t[14]
    assert 'front of a theater' in t[18]
    assert t[21] == t[14]
    assert t[25] == t[3]
    assert t[29] == t[14]
    assert t[33] == t[3]
    assert 'nothing to see' in t[37]
    assert 'Go Northwest' in t[42]
    assert t[43] == t[3]
    assert 'Game Over' in t[47]
    print("Tests passed.")
