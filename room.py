from connection import Connection
from output import Output


class Room:
    def __init__(self, name, desc='You are in a maze of twisty passages, all alike', short_desc='a maze',
                 help='It looks like you are completely lost'):
        self._name = str(name)
        self._desc = str(desc)
        self._short_desc = str(short_desc)
        self._help = str(help)
        self._connections = dict()  # direction -> connection
        self._output = Output.getinstance()

    def connect(self, direction, target):
        self._connections[direction] = Connection(direction, self, target)

    @property
    def name(self):
        return self._name

    @property
    def desc(self):
        return self._desc

    @property
    def short_desc(self):
        return self._short_desc

    @property
    def help(self):
        return self._help

    def __str__(self):
        return self._name

    def show(self):
        # TODO use Output method
        self._output.print_sentence(self.desc)

    def show_connecting(self):
        for (direction, connection) in self._connections.items():
            self._output.print_sentence(
                "%s is %s." % (direction.get_random_representation(), connection.target.short_desc))

    def get_connecting(self, direction):
        return self._connections[direction].target
