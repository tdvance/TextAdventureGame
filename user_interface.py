import textwrap


class UserInterface:
    def __init__(self, commands):
        self._commands = commands
        self._text_wrapper = textwrap.TextWrapper(initial_indent='   ',
                                                  fix_sentence_endings=True,
                                                  break_long_words=False)

    def print(self, fmt, *args):
        print('\n'.join(self._text_wrapper.wrap(fmt % args)))

    def describe_room(self, room):
        self.print('%s.', room.desc)
        for (direction, connection) in room._connections.items():
            self.print("%s is %s." % (direction.get_random_representation(),
                                      connection.target.short_desc))
