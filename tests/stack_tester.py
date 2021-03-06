"""Unit tests for the Stack class"""


import unittest

from data_structures.stack import Stack, StackException


class StackTester(unittest.TestCase):

    def setUp(self):
        self.s = Stack()

    def test_stack(self):

        self.assertTrue(self.s.isEmpty())
        with self.assertRaises(StackException):
            self.s.pop()
        with self.assertRaises(StackException):
            self.s.peek()
        self.s.push(2)
        self.assertFalse(self.s.isEmpty())
        self.assertEqual(1, self.s.size())
        self.assertEqual(2, self.s.pop())
        self.assertTrue(self.s.isEmpty())
        self.assertEqual(0, self.s.size())

    def test_stack_stress(self):
        a = list(range(1000000))
        for i in a:
            self.s.push(i)
        for i in a:
            self.assertEqual(len(a), self.s.size())
            self.assertEqual(a.pop(), self.s.pop())


if __name__ == "__main__":
    unittest.main()
