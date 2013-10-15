from unittest import TestCase
from structures.stack import *

__author__ = 'Dmitry Mekhantev'


class TestStack(TestCase):
    def test_push(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        for i in range(9, -1, -1):
            self.assertEqual(stack.pop(), i)

    def test_pop(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        for i in range(4, -1, -1):
            self.assertEqual(stack.pop(), i)
        self.assertRaises(Exception, stack.pop)

    def test_peek(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.peek(), 4)
        for i in range(4, -1, -1):
            self.assertEqual(stack.pop(), i)
        self.assertRaises(Exception, stack.peek)

    def test_min(self):
        stack = Stack()
        for i in (2, 4, 5):
            stack.push(i)
        self.assertEqual(stack.min(), 2)
        stack.push(1)
        self.assertEqual(stack.min(), 1)
        for i in range(4):
            stack.pop()
        self.assertRaises(Exception, stack.min)


class TestSetOfStacks(TestCase):
    def test_push(self):
        stack = SetOfStacks()
        for i in range(10):
            stack.push(i)
        self.assertEqual([stack.pop() for i in range(10)],
                         [i for i in range(9, -1, -1)])

    def test_pop(self):
        stack = SetOfStacks()
        for i in range(10):
            stack.push(i)
        self.assertEqual([stack.pop() for i in range(10)],
                         [i for i in range(9, -1, -1)])
        self.assertRaises(Exception, stack.pop)

    def test_peek(self):
        stack = SetOfStacks()
        for i in range(10):
            stack.push(i)
        self.assertEqual(stack.peek(), 9)
        self.assertEqual([stack.pop() for i in range(10)],
                         [i for i in range(9, -1, -1)])
        self.assertRaises(Exception, stack.peek)


class TestStackSort(TestCase):
    def test_sort(self):
        stack = [2, 4, 2, 9, 1, 7]
        result = sort(stack)
        self.assertEqual(result, sorted(stack))


class TestFixedTripleStack(TestCase):
    def test_push(self):
        stack = FixedTripleStack()
        values = ((0, 1, 2, 3, 2, 3),
                  (2, 8, 6, 9, 7, 2, 7),
                  (9, 2, 3, 1, 5, 6, 2, 4, 1, 5))
        for i, t in enumerate(values):
            for y in t:
                stack.push(i, y)
        self.assertEqual(stack.pop(0), 3)
        for i in range(4):
            stack.pop(1)
        self.assertEqual(stack.pop(1), 6)
        self.assertRaises(Exception, stack.push, 2, 1)

    def test_pop(self):
        stack = FixedTripleStack()
        values = ((0, 1, 2, 3, 2, 3),
                  (2, 8, 6, 9, 7, 2, 7),
                  (9, 2, 3, 1, 5, 6))
        for i, t in enumerate(values):
            for y in t:
                stack.push(i, y)
        self.assertEqual(stack.pop(2), 6)
        for i in range(7):
            stack.pop(1)
        self.assertRaises(Exception, stack.pop, 1)

    def test_peek(self):
        stack = FixedTripleStack()
        values = ((0, 1, 2, 3, 2, 3),
                  (2, 8, 6, 9, 7, 2, 7),
                  (9, 2, 3, 1, 5, 6))
        for i, t in enumerate(values):
            for y in t:
                stack.push(i, y)
        self.assertEqual(stack.peek(0), 3)
        for i in range(6):
            stack.pop(2)
        self.assertRaises(Exception, stack.peek, 2)


class TestHanoiTower(TestCase):
    def test_move_disks(self):
        expected_result = [1, 2, 5, 6, 8, 9, 12, 14]
        source = list(expected_result)
        destination = []
        buffer = []
        move_disks(len(source), source, destination, buffer)
        self.assertEqual(destination, expected_result)