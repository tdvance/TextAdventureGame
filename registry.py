import sys


class Registry:
    class Entry:
        def __init__(self, name, description, short_description, categories, obj):
            self.name = str(name)
            self.description = str(description)
            self.short_description = str(short_description)
            if isinstance(categories, str):
                self.categories = (categories,)
            else:
                self.categories = tuple([str(x) for x in categories])
            assert self.categories
            self.obj = obj

        def __str__(self):
            return "%s:%s(desc=%r, sdesc=%r, cat=%r, obj=%r)" % (
                self.categories[0], self.name, self.description, self.short_description, self.categories, self.obj)

    def __init__(self):
        self._master = dict()  # (name, primary_category) -> Entry
        self._by_primary_category = dict()  # primary_category -> (dict: name->Entry)
        self._by_category = dict()  # any_category -> set(Entry)
        self._debug = False

    def debug(self, fmt, *args):
        if self._debug:
            print("Debug: ", end='')
            print(fmt % args)

    def add_synonym(self, name, real_name, *categories):
        self.debug("add_synonym(%s, %s, *%s)", name, real_name, categories)
        e = self.find(real_name, *categories)
        if e is None:
            raise Exception("%s not found" % real_name)
        self._master[name] = e
        p = e.categories[0]
        key = (name, p)
        if p not in self._by_primary_category:
            self._by_primary_category[p] = dict()
        self._by_primary_category[p][name] = e

    def add(self, name, categories, description=None, short_description=None, obj=None):
        if not description:
            description = name
        if not short_description:
            short_description = description
        e = Registry.Entry(name, description, short_description, categories, obj)
        p = e.categories[0]
        key = (name, p)
        assert key not in self._master
        self._master[key] = e
        if p not in self._by_primary_category:
            self._by_primary_category[p] = dict()
        self._by_primary_category[p][name] = e
        for c in e.categories:
            if c not in self._by_category:
                self._by_category[c] = set()
            self._by_category[c].add(e)
        return e

    def find(self, name, *categories):
        assert categories
        for c in categories:
            key = (name, c)
            if key in self._master:
                return self._master[key]
        for c in categories:
            for e in self._by_category[c]:
                if e.name == name:
                    return e
        return None

    def count_by_primary_category(self, primary_category):
        if primary_category in self._by_primary_category:
            return len(self._by_primary_category)
        else:
            return 0

    def count_by_category(self, category):
        if category in self._by_category:
            return len(self._by_category)
        else:
            return 0

    def dump(self, file=sys.stdout):
        for e in self._master.values():
            print(e, file=file)
