from unittest import TestCase
from structures.graph import *

__author__ = 'Dmitry Mekhantev'


class TestGraph(TestCase):
    def test_search(self):
        node = GraphNode()
        start = node
        node.links.extend((GraphNode(), GraphNode(), GraphNode()))
        node.links[0].links.extend((GraphNode(), GraphNode()))
        node.links[1].links.extend((GraphNode(), GraphNode(), GraphNode()))
        node.links[2].links.extend((GraphNode(), GraphNode()))
        node = node.links[2]
        node.links.extend((GraphNode(), GraphNode()))
        self.assertTrue(search(start, node.links[1]))
        self.assertFalse(search(start, GraphNode()))