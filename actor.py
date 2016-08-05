from item import Item


class Actor(Item):
    def __init__(self, name, desc='There is an actor in the room', p_desc='Strangely enough, you have an actor',
                 t_desc='You picked up the actor', d_desc='You dropped the actor',
                 help_text='This is a placeholder actor that should not actually exist in the game',
                 gettable=False, visible=True):
        Item.__init__(self, name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
