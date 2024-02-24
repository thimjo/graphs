class DirectedGraph:
    def __init__(self):
        self.nodes = set()
        self.weighted_edges = set()
        self.predecessors_of = {}
        self.successors_of = {}

    @staticmethod
    def build_from_nodes_and_edges(nodes: set[int], edges: set[tuple[[int, int], int]]) -> 'DirectedGraph':
        graph = DirectedGraph.build_from_edges(edges)
        graph._add_nodes(nodes)

        return graph

    @staticmethod
    def build_from_edges(edges: set[tuple[[int, int], int]]) -> 'DirectedGraph':
        graph = DirectedGraph()
        graph._add_edges(edges)

        return graph

    def _add_nodes(self, nodes: set[int]):
        for node in nodes:
            self._add_node(node)
            if node not in self.predecessors_of:
                self.predecessors_of[node] = set()

            if node not in self.successors_of:
                self.successors_of[node] = set()

    def _add_edges(self, edges: set[tuple[[int, int], int]]):
        for edge in edges:
            self._add_edge(edge)

    def _add_node(self, node: int):
        self.nodes.add(node)

    def _add_edge(self, edge: tuple[[int, int], int]):
        self.weighted_edges.add(edge)

        ((pred, suc), w) = edge
        self._add_node(pred)
        self._add_node(suc)
        self._add_predecessor_of(suc, pred)
        self._add_successors_of(pred, suc)

    def _add_predecessor_of(self, node: int, pred: int):
        if node not in self.predecessors_of:
            self.predecessors_of[node] = set()
        self.predecessors_of[node].add(pred)

    def _add_successors_of(self, node: int, suc: int):
        if node not in self.predecessors_of:
            self.successors_of[node] = set()
        self.successors_of[node].add(suc)