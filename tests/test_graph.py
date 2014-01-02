from unittest import TestCase
from structures.graph import *


class TestGraph(TestCase):
    def test_search(self):
        node = GraphNode()
        start = node
        node.links += (GraphNode(), GraphNode(), GraphNode())
        node.links[0].links += (GraphNode(), GraphNode())
        node.links[1].links += (GraphNode(), GraphNode(), GraphNode())
        node.links[2].links += (GraphNode(), GraphNode())
        node = node.links[2]
        node.links += (GraphNode(), GraphNode())
        self.assertTrue(search(start, node.links[1]))
        self.assertFalse(search(start, GraphNode()))