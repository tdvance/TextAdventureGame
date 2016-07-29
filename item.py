from noun import Noun


class Item(Noun):
    def __init__(self, name, desc=None, brief_desc=None):
        Noun.__init__(self, self.__class__, name, desc, brief_desc)

    def __getitem__(self, item):
        pass

    def get_preposition(self, item):
        pass

    def __contains__(self, item):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def add_item(self, item, preposition):
        pass

    def __delitem__(self, item):
        pass

    def spawn(self, prepostion, where):
        pass

    def kill(self):
        pass
