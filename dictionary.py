class Entry:
    def __init__(self, term, categories, antonyms, synonyms):
        self._term = str(term)
        self._synonyms = {str(x) for x in synonyms}
        self._antonyms = set()
        self._primary_antonym = None
        for x in antonyms:
            if self._primary_antonym is None:
                self._primary_antonym = str(x)
            self._antonyms.add(str(x))
        self._categories = {str(x) for x in categories}


class Dictionary:
    def __init__(self):
        self._terms = dict()  # term, entry
        self.load_dictionary()

    def load_dictionary(self):  # TODO: load from file
        """

        """
        self.add('north', 'direction', 'south')
        self.add('east', 'direction', 'west')
        self.add('up', 'direction', 'down')
        self.add('left', 'direction', 'right')
        self.add('forward', 'direction', 'backward')

    def add(self, term, categories=[], antonyms=[], synonyms=[]):
        """

        :param term:
        :param categories:
        :param antonyms:
        :param synonyms:
        """
        if isinstance(synonyms, str):
            synonyms = [synonyms]
        if isinstance(antonyms, str):
            antonyms = [antonyms]
        if isinstance(categories, str):
            categories = [categories]
        e = Entry(term, categories, antonyms, synonyms)
        self._terms[term] = e

    def lookup(self, term):  # TODO: optimize
        """

        :param term:
        :return:
        """
        term = str(term)  # make sure it is a string
        if term in self._terms:  # first, find primary terms
            return self._terms[term]
        for e in self._terms.values():  # then look at synonyms
            if term in e._synonyms:
                return e
        # now, see if it is an abbreviation of a term
        for t in self._terms:
            if t.startswith(term):
                return self._terms[t]
        # and...the same for synonyms
        for e in self._terms.values():
            for t in e._synonyms:
                if t.startswith(term):
                    return e
        # not found
        return None
