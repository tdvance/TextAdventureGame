from direction import Direction


class Connection:
    def __init__(self, direction, source, target):
        assert isinstance(direction, Direction)
        assert 'Room' in str(type(source))
        assert type(source) == type(target)
        self._direction = direction
        self._source = source
        self._target = target

    @property
    def direction(self):
        return self._direction

    @property
    def source(self):
        return self._source

    @property
    def target(self):
        return self._target

    def __str__(self):
        return str((self._direction, self._target))
