from actor import Actor


class Enemy(Actor):
    """
    An enemy is an actor that has health.  An enemy is alive if and only health is positive.
    """

    def __init__(self, name, desc=None, brief_desc=None, max_health=1.0):
        Actor.__init__(self, name, desc, brief_desc)
        self._max_health = float(max_health)
        self._health = self._max_health

    @property
    def health(self):
        return self._health

    def add_health(self, amount):
        self._health = max(min(self._max_health + float(amount), self._max_health), 0.0)

    def subtract_health(self, amount):
        self.add_health(-float(amount))

    @property
    def alive(self):
        return self.health > 0.0

    @property
    def max_health(self):
        return self._max_health

    def set_max_health(self):
        self._health = self.max_health

    def kill(self):
        self._health = 0.0
