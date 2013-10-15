from unittest import TestCase
from structures.string import *

__author__ = 'Dmitry Mekhantev'


class TestString(TestCase):
    def test_reverse(self):
        result = reverse('abcdefg')
        self.assertEqual(result, 'gfedcba')

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
        result = compress('aabbbcddeffff')
        self.assertEqual(result, 'a2b3c1d2e1f4')

    def test_is_rotation(self):
        b = is_rotation('abcde', 'cdeab')
        self.assertEqual(b, True)
        b = is_rotation('abcde', 'cdeba')
        self.assertEqual(b, False)