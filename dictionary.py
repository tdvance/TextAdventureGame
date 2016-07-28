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

    def __str__(self):
        return self._term

    def __repr__(self):
        return "Entry(%r, %r, %r, %r)" % (self._term, self._categories, self._antonyms, self._synonyms)


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

        self.add('go', 'command')
        a = {e for e in self._terms.values() if e._primary_antonym is not None}
        for t in a:
            x = t._antonyms
            x.discard(t._primary_antonym)
            self.add(t._primary_antonym, t._categories, t._synonyms, x)

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

    def lookup(self, term, expected_category=None):  # TODO: optimize
        """

        :param term:
        :return:
        """
        term = str(term)  # make sure it is a string
        if expected_category is not None:
            expected_category = str(expected_category)
        if term in self._terms:  # first, find primary terms
            if expected_category is None or expected_category in self._terms[term]._categories:
                return self._terms[term]
        for e in self._terms.values():  # then look at synonyms
            if term in e._synonyms:
                if expected_category is None or expected_category in e._categories:
                    return e
        # now, see if it is an abbreviation of a term
        for t in self._terms:
            if t.startswith(term):
                if expected_category is None or expected_category in self._terms[t]._categories:
                    return self._terms[t]
        # and...the same for synonyms
        for e in self._terms.values():
            for t in e._synonyms:
                if t.startswith(term):
                    if expected_category is None or expected_category in e._categories:
                        return e
        # not found
        return None
