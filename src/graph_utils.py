from src.directed_graph import DirectedGraph


def has_positive_weights(graph: DirectedGraph):
    for (edge, weight) in graph.weighted_edges:
        if weight < 0:
            return False

    return True


def depth_first_search(graph: DirectedGraph, root: int) -> list[int]:
    visited_nodes_list = [root]
    visited_nodes_set = {root}
    __depth_first_search(graph, root, visited_nodes_list, visited_nodes_set)

    return visited_nodes_list


def __depth_first_search(graph: DirectedGraph, node: int, visited_nodes_list: list[int], visited_nodes_set: set[int]):
    successors = graph.successors_of[node]
    unvisited_successors = filter(lambda n: n not in visited_nodes_set, successors)
    [
        (
            visited_nodes_list.append(suc),
            visited_nodes_set.add(suc),
            __depth_first_search(graph, suc, visited_nodes_list, visited_nodes_set)
        )
        for suc in unvisited_successors
    ]


def breadth_first_search(graph: DirectedGraph, root: int) -> list[int]:
    visited_nodes_list = [root]
    visited_nodes_set = {root}
    __breadth_first_search(graph, root, visited_nodes_list, visited_nodes_set)

    return visited_nodes_list


def __breadth_first_search(graph: DirectedGraph, node: int, visited_nodes_list: list[int], visited_nodes_set: set[int]):
    successors = graph.successors_of[node]
    unvisited_successors = [n for n in successors if n not in visited_nodes_set]
    [(visited_nodes_list.append(suc), visited_nodes_set.add(suc)) for suc in unvisited_successors]
    [__breadth_first_search(graph, suc, visited_nodes_list, visited_nodes_set) for suc in unvisited_successors]
