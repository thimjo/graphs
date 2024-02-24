from src.directed_graph import DirectedGraph


def has_positive_weights(graph: DirectedGraph):
    for (edge, weight) in graph.weighted_edges:
        if weight < 0:
            return False

    return True