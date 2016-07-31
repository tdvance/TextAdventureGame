import csv
import os

from collections import namedtuple

class Resources:
    def __init__(self, resources_directory='Resources'):
        self._resources_directory = resources_directory
        self._master = dict()
        self._synonyms = dict()

    def normalize(self, name, category):
        name = name.lower()
        category = category.lower
        while name in self._synonyms and (name, category) not in self._master:
            name = self._synonyms[name]
        return name, category

    def add(self, name, category, value):
        self._master[self.normalize(name, category)] = value

    def add_synonym(self, name, real_name):
        self._synonyms[name.lower()] = real_name

    def get(self, name, category):
        return self._master[self.normalize(name, category)]

    def has(self, name, category):
        return self.normalize(name, category) in self._master

    def load_resource(self, category, name_field=0):
        first_name = None
        filename = os.path.join(self._resources_directory, "%s.csv" % category)
        with open(filename) as f:
            f_csv = csv.reader(f)
            headers = next(f_csv)
            Resource = namedtuple(category, headers)
            for row in f_csv:
                if row and not row[0].strip().startswith('#'):
                    row = [x for x in row]
                    assert len(row) <= len(headers)
                    while len(row) < len(headers):
                        row.append('')
                    value = Resource(*row)
                    name = row[name_field]
                    if category == 'Synonyms':
                        self.add_synonym(name, row[1])
                    else:
                        self.add(name, category, value)
                    if not first_name:
                        first_name = name  # sometimes, the first resource is significant
        return first_name
