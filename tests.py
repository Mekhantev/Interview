from unittest import TestCase
from functions import reverse, all_chars_single, binary_search, permutation, \
    replace_spaces, compress_string, rotate, set_zeros, is_rotation
import linked_list
from stack import FixedTripleStack, Stack, SetOfStacks

__author__ = 'Dmitry Mekhantev'


class TestFunctions(TestCase):
    def test_reverse(self):
        result = reverse('abcdefg')
        self.assertEqual(result, 'gfedcba')

    def test_binary_search(self):
        ints = [0, 3, 6, 7, 12, 22, 31, 49]
        result = binary_search(ints, 7, 0, len(ints))
        self.assertEqual(result, 3)

    def test_all_chars_single(self):
        self.assertEqual(all_chars_single('abdhs'), True)
        self.assertEqual(all_chars_single('abdahs'), False)

    def test_permutation(self):
        b = permutation('bghjk', 'bghjk')
        self.assertEqual(b, True)
        b = permutation('bghjik', 'beghjk')
        self.assertEqual(b, False)
        b = permutation('bghji', 'beghjk')
        self.assertEqual(b, False)

    def test_replace_spaces(self):
        result = replace_spaces('sds dwdw sdad')
        self.assertEqual(result, 'sds%20dwdw%20sdad')

    def test_compress_string(self):
        result = compress_string('aabbbcddeffff')
        self.assertEqual(result, 'a2b3c1d2e1f4')

    def test_rotate(self):
        matrix = [[10, 11, 12, 13],
                  [14, 15, 16, 17],
                  [18, 19, 20, 21],
                  [22, 23, 24, 25]]

        expected_matrix = [[22, 18, 14, 10],
                           [23, 19, 15, 11],
                           [24, 20, 16, 12],
                           [25, 21, 17, 13]]
        self.assertEqual(rotate(matrix), expected_matrix)

    def test_set_zeros(self):
        matrix = [[10, 11, 12, 13],
                  [14, 15, 16, 17],
                  [18, 19, 0, 21],
                  [22, 23, 24, 25]]
        expected_matrix = [[10, 11, 0, 13],
                           [14, 15, 0, 17],
                           [0, 0, 0, 0],
                           [22, 23, 0, 25]]
        self.assertEqual(set_zeros(matrix), expected_matrix)

    def test_is_rotation(self):
        b = is_rotation('abcde', 'cdeab')
        self.assertEqual(b, True)
        b = is_rotation('abcde', 'cdeba')
        self.assertEqual(b, False)


class TestStructures(TestCase):
    def test_delete_dups(self):
        source_linked_list = linked_list.make([2, 1, 3, 2, 7, 6, 3, 5, 1, 9])
        expected_linked_list = linked_list.make([2, 1, 3, 7, 6, 5, 9])
        result = linked_list.delete_dups(source_linked_list)
        self.assertEqual(expected_linked_list, result)

    def test_get_from_end(self):
        source_linked_list = linked_list.make([2, 1, 3, 2, 7, 6, 3, 5, 1, 9])
        result = linked_list.get_from_end(source_linked_list, 4)
        self.assertEqual(6, result.data)

    def test_delete_node(self):
        source_linked_list = linked_list.make([2, 1, 3, 2, 7, 6, 3, 5, 1, 9])
        expected_linked_list = linked_list.make([2, 1, 3, 7, 6, 3, 5, 1, 9])
        #delete [3] element
        linked_list.delete_node(source_linked_list.next.next.next)
        self.assertEqual(expected_linked_list, source_linked_list)

    def test_partition(self):
        source_linked_list = linked_list.make([1, 4, 8, 5, 3, 7, 2, 3])
        expected_linked_list = linked_list.make([1, 2, 3, 4, 8, 5, 7, 3])
        result = linked_list.partition(source_linked_list, 3)
        self.assertEqual(expected_linked_list, result)

    def test_custom_sum(self):
        linked_list1 = linked_list.make([8, 4, 8, 5])
        linked_list2 = linked_list.make([5, 2, 3, 4])
        expected_linked_list = linked_list.make([1, 6, 1, 0, 4])
        result = linked_list.custom_sum(linked_list1, linked_list2)
        self.assertEqual(expected_linked_list, result)

    def test_get_loop_beginning(self):
        source_linked_list = linked_list.make([2, 1, 3, 5, 7, 6, 9])
        loop_beginning = None
        n = source_linked_list
        beginning_value = 5
        while n:
            if n.data == beginning_value:
                loop_beginning = n
            if n.data == 9:
                n.next = loop_beginning
                break
            n = n.next
        result = linked_list.get_loop_beginning(source_linked_list)
        self.assertEqual(beginning_value, result.data)

    def test_is_palindrome(self):
        l = linked_list.make([0, 1, 2, 3, 2, 1, 0])
        b = linked_list.is_palindrome(l)
        self.assertEqual(b, True)
        l = linked_list.make([0, 1, 2, 3, 4, 2, 1, 0])
        b = linked_list.is_palindrome(l)
        self.assertEqual(b, False)
        l = linked_list.make([0, 1, 2, 3, 6, 1, 0])
        b = linked_list.is_palindrome(l)
        self.assertEqual(b, False)


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


class TestStack(TestCase):
    def test_push(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        self.assertEqual(stack.buffer, [i for i in range(10)])

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























