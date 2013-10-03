from unittest import TestCase
from functions import reverse, all_chars_single, binary_search, permutation, \
    replace_spaces, compress_string, rotate, set_zeros, is_rotation
from structures import delete_dups, make_linked_list, get_from_end, delete_node

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
        source_linked_list = make_linked_list([2, 1, 3, 2, 7, 6, 3, 5, 1, 9])
        expected_linked_list = make_linked_list([2, 1, 3, 7, 6, 5, 9])
        result = delete_dups(source_linked_list)
        self.assertEqual(expected_linked_list, result)

    def test_get_from_end(self):
        source_linked_list = make_linked_list([2, 1, 3, 2, 7, 6, 3, 5, 1, 9])
        result = get_from_end(source_linked_list, 4)
        self.assertEqual(6, result.data)

    def test_delete_node(self):
        source_linked_list = make_linked_list([2, 1, 3, 2, 7, 6, 3, 5, 1, 9])
        expected_linked_list = make_linked_list([2, 1, 3, 7, 6, 3, 5, 1, 9])
        #delete [3] element
        delete_node(source_linked_list.next_node.next_node.next_node)
        self.assertEqual(expected_linked_list, source_linked_list)






