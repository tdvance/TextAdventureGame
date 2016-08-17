import os

from command import Command
from direction import Direction
from error import Error
from room import Room


def load(resource_name, resource_dir='Resources'):
    with open(os.path.join(resource_dir, resource_name + '.res')) as f:
        rows = []
        for line in f:
            l = line
            if '#' in l:
                i = l.index('#')
                l = l[0:i]
            l = l.strip()
            if l:
                row = l.split(',')
                for i in range(len(row)):
                    row[i] = row[i].strip()
                rows.append(row)
    return rows


def load_directions():
    d = dict()
    rows = load('Directions')
    for row in rows:
        name = row[0]
        representations = row[1:]
        d[str(name).lower()] = Direction(name, *representations)
    return d


def load_commands(game):
    d = dict()
    rows = load('Commands')
    for row in rows:
        name = row[0]
        obj = row[1].lower()
        method = row[2].lower()
        help_text = row[3]
        if obj == 'game':
            obj = game
        elif obj == 'player':
            obj = game.player
        elif obj == 'world':
            obj = game.world
        method = getattr(obj, method)
        d[str(name).lower()] = Command(name, obj, method, help_text)
    return d


def load_rooms(world, directions):
    rows = load('Rooms')
    connections = dict()
    for row in rows:
        name = row[0]
        desc = row[1]
        sdesc = row[2]
        help = row[3]
        r = Room(name, desc, sdesc, help)
        world[name] = r
        if not world.starting_room:
            world.set_starting_room(r)
        connections[name.lower()] = row[4:]
    for name in connections:
        for i in range(0, len(connections[name]), 2):
            d = directions[connections[name][i].lower()]
            t = world[connections[name][i + 1]]
            world[name].connect(d, t)


def load_errors():
    d = dict()
    rows = load('Errors')
    for row in rows:
        name = row[0]
        texts = row[1:]
        d[name.lower()] = Error(name, *texts)
    return d


def load_aliases():
    d = dict()
    rows = load('Aliases')
    for row in rows:
        name = row[0]
        alias_of = row[1]
        d[name.lower()] = alias_of.lower()
    return d
