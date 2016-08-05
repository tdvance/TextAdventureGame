import random


class Error:
    def __init__(self, name, *texts):
        self._name = name
        self._texts = list(texts)

    def get_random_text(self):
        if not self._texts:
            return self._name
        return random.choice(self._texts)
