from unittest import TestCase
from structures.string import *

__author__ = 'Dmitry Mekhantev'


class TestString(TestCase):
    def test_reverse(self):
        result = reverse('abcdefg')
        self.assertEqual(result, 'gfedcba')

    def test_all_chars_single(self):
        self.assertTrue(all_chars_single('abdhs'))
        self.assertFalse(all_chars_single('abdahs'))

    def test_permutation(self):
        self.assertTrue(permutation('bghjk', 'bghjk'))
        self.assertFalse(permutation('bghjik', 'beghjk'))
        self.assertFalse(permutation('bghji', 'beghjk'))

    def test_replace_spaces(self):
        result = replace_spaces('sds dwdw sdad')
        self.assertEqual(result, 'sds%20dwdw%20sdad')

    def test_compress_string(self):
        result = compress('aabbbcddeffff')
        self.assertEqual(result, 'a2b3c1d2e1f4')

    def test_is_rotation(self):
        self.assertTrue(is_rotation('abcde', 'cdeab'))
        self.assertFalse(is_rotation('abcde', 'cdeba'))