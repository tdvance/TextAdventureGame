from room import Room


class Item:
    def __init__(self, name, desc='There is an item in the room', p_desc='You have an item',
                 t_desc='You picked up the item',
                 d_desc='You dropped the item',
                 help='This is a placeholder item that should not actually exist in the game', gettable=True,
                 visible=True, room=None, on_player=False):
        self._name = str(name)
        self._desc = str(desc)
        self._p_desc = str(p_desc)
        self._t_desc = str(t_desc)
        self._d_desc = str(d_desc)
        self._help = str(help)
        self._gettable = bool(gettable)
        self._visible = bool(visible)
        assert isinstance(room, Room)
        self._room = room
        self._on_player = bool(on_player)

    @property
    def name(self):
        return self._name

    @property
    def desc(self):
        return self._desc

    @property
    def p_desc(self):
        return self._p_desc

    @property
    def t_desc(self):
        return self._t_desc

    @property
    def d_desc(self):
        return self._d_desc

    @property
    def help(self):
        return self._help

    @property
    def is_gettable(self):
        return self._gettable

    @property
    def is_visible(self):
        return self._visible

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, value):
        assert isinstance(value, Room)
        self._room = value

    @property
    def on_player(self):
        return self._on_player

    @on_player.setter
    def on_player(self, value):
        if not self.is_gettable:
            raise Exception("Cannot take item that is not gettable")
        self._on_player = bool(value)

    def __str__(self):
        return self.name
