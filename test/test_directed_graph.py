from unittest import TestCase
from src.directed_graph import DirectedGraph


class TestDirectedGraph(TestCase):
    def test_build_directed_graph(self):
        nodes = {1, 2, 3}
        edges = {((1, 2), -1)}

        graph = DirectedGraph.build_from_nodes_and_edges(nodes, edges)

        for node in nodes:
            self.assertIn(node, graph.nodes)

        for edge in edges:
            self.assertIn(edge, graph.weighted_edges)

        self.assertIn(2, graph.successors_of[1])
        self.assertIn(1, graph.predecessors_of[2])
        self.assertNotIn(3, graph.successors_of[1])
        self.assertNotIn(3, graph.predecessors_of[2])
        self.assertFalse(graph.predecessors_of[3])
        self.assertFalse(graph.successors_of[3])
