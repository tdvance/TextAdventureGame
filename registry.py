from collections import defaultdict

import game_object


class Registry:
    def __init__(self):
        self._by_name = defaultdict(set)  # {name:{GameObject}}
        self._by_cls = defaultdict(set)  # {class:{GameObject}}
        self._by_both = dict()  # {(name, class):{GameObject}}

    def count(self, cls):
        if cls in self._by_cls:
            return len(self._by_cls[cls])
        else:
            return 0

    def iter(self, cls):
        if cls in self._by_cls:
            return iter(self._by_cls[cls])
        else:
            return iter([])

    def add(self, obj):
        name = str(obj)
        cls = type(obj)
        self._by_name[name].add(obj)
        self._by_cls[cls].add(obj)

    def delete(self, obj):
        if isinstance(obj, game_object.GameObject):
            self._by_name[str(obj)].remove(obj)
            self._by_cls[type(obj)].remove(obj)
            self._by_both[(str(obj), type(obj))].remove(obj)
        else:
            raise NotImplementedError(type(obj))

    def get(self, obj, cls=None):
        name = str(obj)
        if cls is None and isinstance(obj, game_object.GameObject):
            cls = type(obj)
        if cls is None:
            raise Exception("Cannot determine class of %r" % obj)
        t = (name, cls)
        if t in self._by_both:
            return self._by_both[t]
        return None

    def find(self, obj, look_in):
        if isinstance(obj, game_object.GameObject):
            return self.get(obj)
        s = self._by_name(str(obj))
        for x in s:
            cls = type(x)
            if cls in look_in:
                return x
        return None
