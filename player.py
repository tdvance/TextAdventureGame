from actor import Actor


class Player(Actor):
    def __init__(self, player='Player', desc=None, brief_desc=None):
        Actor.__init__(self, player, desc, brief_desc)
