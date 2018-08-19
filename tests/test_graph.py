from unittest import TestCase
from redvelvet.graph.graph import Graph


class TestGraph(TestCase):

    def test_len(self):
        graph = Graph(directed=True)
        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')
        self.assertEqual(len(graph), 3)

