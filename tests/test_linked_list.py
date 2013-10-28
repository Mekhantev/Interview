from unittest import TestCase
from structures.linked_list import *


class TestLinkedList(TestCase):
    def test_delete_dups(self):
        source_linked_list = make([2, 1, 3, 2, 7, 6, 3, 5, 1, 9])
        expected_linked_list = make([2, 1, 3, 7, 6, 5, 9])
        result = delete_dups(source_linked_list)
        self.assertEqual(expected_linked_list, result)

    def test_get_from_end(self):
        source_linked_list = make([2, 1, 3, 2, 7, 6, 3, 5, 1, 9])
        result = get_from_end(source_linked_list, 4)
        self.assertEqual(6, result.data)

    def test_delete_node(self):
        source_linked_list = make([2, 1, 3, 2, 7, 6, 3, 5, 1, 9])
        expected_linked_list = make([2, 1, 3, 7, 6, 3, 5, 1, 9])
        #delete [3] element
        delete_node(source_linked_list.next.next.next)
        self.assertEqual(expected_linked_list, source_linked_list)

    def test_partition(self):
        source_linked_list = make([1, 4, 8, 5, 3, 7, 2, 3])
        expected_linked_list = make([1, 2, 3, 4, 8, 5, 7, 3])
        result = partition(source_linked_list, 3)
        self.assertEqual(expected_linked_list, result)

    def test_custom_sum(self):
        linked_list1 = make([8, 4, 8, 5])
        linked_list2 = make([5, 2, 3, 4])
        expected_linked_list = make([1, 6, 1, 0, 4])
        result = custom_sum(linked_list1, linked_list2)
        self.assertEqual(expected_linked_list, result)

    def test_get_loop_beginning(self):
        source_linked_list = make([2, 1, 3, 5, 7, 6, 9])
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
        result = get_loop_beginning(source_linked_list)
        self.assertEqual(beginning_value, result.data)

    def test_is_palindrome(self):
        l = make([0, 1, 2, 3, 2, 1, 0])
        self.assertTrue(is_palindrome(l))
        l = make([0, 1, 2, 3, 4, 2, 1, 0])
        self.assertFalse(is_palindrome(l))
        l = make([0, 1, 2, 3, 6, 1, 0])
        self.assertFalse(is_palindrome(l))