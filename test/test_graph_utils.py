from unittest import TestCase
from src.directed_graph import DirectedGraph
from src.graph_utils import has_positive_weights


class TestGraphUtils(TestCase):
    def test_graph_with_positive_weights(self):
        edges = {
            ((1, 2), 1),
            ((1, 3), 2)
        }
        graph = DirectedGraph.build_from_edges(edges)

        self.assertTrue(has_positive_weights(graph))

    def test_graph_with_non_positive_weights(self):
        edges = {
            ((1, 2), 1),
            ((1, 3), -3)
        }
        graph = DirectedGraph.build_from_edges(edges)

        self.assertFalse(has_positive_weights(graph))
