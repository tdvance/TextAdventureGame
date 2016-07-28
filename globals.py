reverse_directions = {
    'north': 'south',
    'east': 'west',
    'left': 'right',
    'up': 'down',
    'forward': 'backward',
    'in':'out'
}

rev = dict()
for k,v in reverse_directions.items():
    rev[v] = k
reverse_directions.update(rev)
del rev

