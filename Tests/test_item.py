from unittest import TestCase

from item import Item


class TestItem(TestCase):
    def test___init__(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
        exp_result = name
        result = instance._name
        self.assertEqual(exp_result, result)
        exp_result = desc
        result = instance._desc
        self.assertEqual(exp_result, result)
        exp_result = p_desc
        result = instance._p_desc
        self.assertEqual(exp_result, result)
        exp_result = t_desc
        result = instance._t_desc
        self.assertEqual(exp_result, result)
        exp_result = d_desc
        result = instance._d_desc
        self.assertEqual(exp_result, result)
        exp_result = help_text
        result = instance._help
        self.assertEqual(exp_result, result)
        exp_result = gettable
        result = instance._gettable
        self.assertEqual(exp_result, result)
        exp_result = visible
        result = instance._visible
        self.assertEqual(exp_result, result)
        self.assertFalse(instance.on_player)
        self.assertIsNone(instance.room)


class TestAction(TestCase):
    def test_name(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
        exp_result = name
        result = instance.name
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_desc(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
        exp_result = desc
        result = instance.desc
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_p_desc(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
        exp_result = p_desc
        result = instance.p_desc
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_d_desc(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
        exp_result = d_desc
        result = instance.d_desc
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_t_desc(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
        exp_result = t_desc
        result = instance.t_desc
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_help(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
        exp_result = help_text
        result = instance.help
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_is_gettable(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
        exp_result = gettable
        result = instance.is_gettable
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_is_visible(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
        exp_result = visible
        result = instance.is_visible
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_room(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        room = None
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible, room)
        exp_result = room
        result = instance.room
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_room_setter(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        room = None
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
        instance.room = room
        exp_result = room
        result = instance.room
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_on_player(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        room = None
        on_player = True
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible, room, on_player)
        exp_result = on_player
        result = instance.on_player
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_on_player_setter(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = True
        visible = True
        room = None
        on_player = True
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible, room)
        instance.on_player = on_player
        exp_result = on_player
        result = instance.on_player
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_str(self):
        name = 'An item'
        desc = 'There is an item in the room'
        p_desc = 'You have an item'
        t_desc = 'You picked up the item'
        d_desc = 'You dropped the item'
        help_text = 'This is a placeholder item that should not actually exist in the game'
        gettable = False
        visible = True
        instance = Item(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
        exp_result = name
        result = str(instance)
        self.assertEqual(exp_result, result)
