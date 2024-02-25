from src.directed_graph import DirectedGraph


def has_positive_weights(graph: DirectedGraph):
    for (edge, weight) in graph.weighted_edges:
        if weight < 0:
            return False

    return True


def depth_first_search(graph: DirectedGraph, root: int) -> list[int]:
    visited_nodes_list = []
    visited_nodes_set = set()
    _depth_first_search(graph, root, visited_nodes_list, visited_nodes_set)

    return visited_nodes_list


def _depth_first_search(graph: DirectedGraph, node: int, visited_nodes_list: list[int], visited_nodes_set: set[int]):
    visited_nodes_list.append(node)
    visited_nodes_set.add(node)

    successors = graph.successors_of[node]
    unvisited_successors = filter(lambda n: n not in visited_nodes_set, successors)
    [_depth_first_search(graph, n, visited_nodes_list, visited_nodes_set) for n in unvisited_successors]
