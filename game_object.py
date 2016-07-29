class GameObject:
    pass


import registry


class GameObject:
    """
    A GameObject has a name, which should be unique for its class.  It has optional
    long and short descriptions.  The string value of a GameObject is just its name.  Usually
    accessed via subclasses rather than directly.
    """

    _registry = registry.Registry()

    @classmethod
    def get(cls, obj, objcls=None):
        if objcls is None:
            if isinstance(obj, GameObject):
                objcls = type(obj)
            else:
                objcls = cls
        return cls._registry.get(obj, objcls)

    def __init__(self, cls, name, desc=None, brief_desc=None):
        self._name = str(name)
        self._cls = cls
        if GameObject._registry.get(self._name, self._cls):
            raise Exception("Name %r already exists for Class %r" % (name, cls))
        GameObject._registry.add(self)
        if desc is None:
            self._desc = name
        else:
            self._desc = desc
        if brief_desc is None:
            self._brief_desc = self._desc
        else:
            self._brief_desc = brief_desc

    @property
    def name(self):
        return self._name

    @property
    def desc(self):
        return self._desc

    @property
    def brief_desc(self):
        return self._brief_desc

    def __str__(self):
        return self._name

    def __repr__(self):
        return "%r(name=%r, desc=%r, brief_desc=%r)" % (self._cls, self._name, self._desc, self._brief_desc)
