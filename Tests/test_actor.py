from unittest import TestCase

from actor import Actor


class TestActor(TestCase):
    def test___init__(self):
        name = 'An actor'
        desc = 'There is an actor in the room'
        p_desc = 'Strangely enough, you have an actor'
        t_desc = 'You picked up the actor'
        d_desc = 'You dropped the actor'
        help_text = 'This is a placeholder actor that should not actually exist in the game'
        gettable = False
        visible = True
        instance = Actor(name, desc, p_desc, t_desc, d_desc, help_text, gettable, visible)
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
