from unittest import TestCase
from Adt import Stack, eval_postfix

class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

class TestSimpleStack(TestStack):

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.items[0])

    def test_pop(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.pop())
        self.assertEqual(0, len(self.stack.items))

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())


class TestEvalExpr(TestStack):
    def test_eval(self):
        self.assertEqual(206, eval_postfix("56 47 + 2 *"))

    def test_seven(self):
        self.assertEqual(7, eval_postfix("1 2 3 * +"))