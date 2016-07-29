from actor import Actor


class Enemy(Actor):
    def __init__(self, name, desc=None, brief_desc=None):
        Actor.__init__(self, name, desc, brief_desc)
