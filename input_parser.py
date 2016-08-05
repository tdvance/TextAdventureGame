from output import Output


class Parser:
    def __init__(self, directions, actions, aliases, errors):
        self._directions = directions
        self._actions = actions
        self._aliases = aliases
        self._errors = errors
        self._output = Output.getinstance()

    def get_input(self, prompt='> '):
        while True:
            s = None
            while not s:
                s = input(prompt)
            l = s.split()
            cmd = l[0].lower()
            args = [x.lower() for x in l[1:]]
            if cmd in self._aliases:
                cmd = self._aliases[cmd]
            for i in range(len(args)):
                if args[i] in self._aliases:
                    args[i] = self._aliases[args[i]]
            # special case: a direction is interpreted as a 'Go' command
            if cmd in self._directions:
                args.insert(0, self._directions[cmd].name)
                cmd = 'Go'
            cmd = cmd.lower()
            if cmd not in self._actions:
                fmt = self._errors['badcommand'].get_random_text()
                self._output.print_sentence(fmt, cmd)
            else:
                cmd = self._actions[cmd]
                return (cmd, *args)
