from unittest import TestCase
from structures.hash_table import *


class TestHashTable(TestCase):
    def test_add(self):
        h = HashTable()
        pair1 = Pair('key1', 'value')
        pair2 = Pair('key2', 'value')
        pair3 = Pair('key12', 'value')
        h.add(pair1)
        h.add(pair2)
        h.add(pair3)
        self.assertEqual(h.get(pair1.key), pair1)
        self.assertEqual(h.get(pair2.key), pair2)
        self.assertEqual(h.get(pair3.key), pair3)
        self.assertRaises(Exception, h.add, pair1)
        for i in range(3, 10):
            h.add(Pair('key'.join(str(i)), 'value'))
        self.assertRaises(Exception, h.add, Pair('key10', 'value'))

    def test_get(self):
        h = HashTable()
        pair1 = Pair('key1', 'value')
        pair2 = Pair('key2', 'value')
        h.add(pair1)
        self.assertEqual(h.get(pair1.key), pair1)
        self.assertRaises(Exception, h.get, pair2.key)
        self.assertRaises(Exception, h.get, 'key12')