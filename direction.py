import random


class Direction:
    def __init__(self, name, *representations):
        self._name = name
        self._representations = list(representations)

    @property
    def name(self):
        return self._name

    def get_random_representation(self):
        if not self._representations:
            return self.name
        return random.choice(self._representations)

    def __str__(self):
        return self.name
