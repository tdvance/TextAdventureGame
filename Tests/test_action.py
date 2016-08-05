from unittest import TestCase

from action import Action
from output import Output


class TestAction(TestCase):
    def test_init(self):
        name = 'Test Name'
        obj = Output.getinstance()
        method = obj.print_sentence
        help_text = 'The print_sentence method of the Output singleton'
        instance = Action(name, obj, method, help_text)
        exp_result = name
        result = instance.name
        self.assertEqual(exp_result, result)
        exp_result = help
        result = instance.help
        self.assertEqual(exp_result, result)
        exp_result = obj
        result = instance._obj
        self.assertEqual(exp_result, result)
        exp_result = method
        result = instance._method
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_name(self):
        name = 'Test Name'
        obj = Output.getinstance()
        method = obj.print_sentence
        help_text = 'The print_sentence method of the Output singleton'
        instance = Action(name, obj, method, help_text)
        exp_result = name
        result = instance.name
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_help(self):
        name = 'Test Name'
        obj = Output.getinstance()
        method = obj.print_sentence
        help_text = 'The print_sentence method of the Output singleton'
        instance = Action(name, obj, method, help_text)
        exp_result = help_text
        result = instance.help
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_call(self):
        name = 'Test Name'
        obj = Output.getinstance()
        method = obj.get_sentence
        help_text = 'The get_sentence method of the Output singleton'
        instance = Action(name, obj, method, help_text)
        exp_result = '\n   Some format 5.  '
        result = instance('some format %d', 5)
        self.assertEqual(exp_result, result)


class TestAction(TestCase):
    def test_str(self):
        name = 'Test Name'
        obj = Output.getinstance()
        method = obj.print_sentence
        help_text = 'The print_sentence method of the Output singleton'
        instance = Action(name, obj, method, help_text)
        exp_result = name
        result = str(instance)
        self.assertEqual(exp_result, result)
