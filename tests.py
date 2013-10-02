from unittest import TestCase
from functions import reverse, all_chars_single, binary_search, permutation, replace_spaces, compress_string

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

