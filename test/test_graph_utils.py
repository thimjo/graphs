from unittest import TestCase
from src.directed_graph import DirectedGraph
from src.graph_utils import has_positive_weights
from src.graph_utils import depth_first_search


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

    def test_depth_first_search(self):
        edges = {
            ((0, 1), 1),
            ((0, 2), 2),
            ((1, 11), 2),
            ((1, 12), 2),
            ((2, 21), 2),
            ((2, 22), 2),
            ((0, 3), 2),
        }
        graph = DirectedGraph.build_from_edges(edges)
        expected_nodes_list = [0, 1, 11, 12, 2, 21, 22, 3]

        visited_nodes = depth_first_search(graph, 0)
        actual_nodes_list = list()
        actual_nodes_list.extend(visited_nodes)

        self.assertEqual(expected_nodes_list, actual_nodes_list)
