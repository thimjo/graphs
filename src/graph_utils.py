from src.directed_graph import DirectedGraph


def has_positive_weights(graph: DirectedGraph):
    for (edge, weight) in graph.weighted_edges:
        if weight < 0:
            return False

    return True

def depth_first_search(graph: DirectedGraph, root: int) -> list[int]:
    visited_nodes = []
    _depth_first_search(graph, root, visited_nodes)

    return visited_nodes


def _depth_first_search(graph: DirectedGraph, node: int, visited_nodes: list[int]):
    visited_nodes.append(node)

    successors = graph.successors_of[node]
    for suc in successors:
        _depth_first_search(graph, suc, visited_nodes)
