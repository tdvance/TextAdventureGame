import textwrap


class Output:
    _instance = None

    @classmethod
    def getinstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self._wrapper = textwrap.TextWrapper(initial_indent='   ', fix_sentence_endings=True,
                                             break_long_words=False)

    def print_sentence(self, fmt, *args):
        t = fmt % args
        t = t.strip()
        t = t[0].upper() + t[1:]
        t = '\n' + '\n'.join(self._wrapper.wrap(t))
        print(t)
