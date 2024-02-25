class DirectedGraph:
    def __init__(self):
        self.nodes = set()
        self.weighted_edges = set()
        self.predecessors_of = {}
        self.successors_of = {}

    @staticmethod
    def build_from_nodes_and_edges(nodes: set[int], edges: set[tuple[[int, int], int]]) -> 'DirectedGraph':
        graph = DirectedGraph.build_from_edges(edges)
        graph.__add_nodes(nodes)

        return graph

    @staticmethod
    def build_from_edges(edges: set[tuple[[int, int], int]]) -> 'DirectedGraph':
        graph = DirectedGraph()
        graph.__add_edges(edges)

        return graph

    def __add_nodes(self, nodes: set[int]):
        for node in nodes:
            self.__add_node(node)

    def __add_edges(self, edges: set[tuple[[int, int], int]]):
        for edge in edges:
            self.__add_edge(edge)

    def __add_node(self, node: int):
        self.nodes.add(node)
        if node not in self.predecessors_of:
            self.predecessors_of[node] = set()

        if node not in self.successors_of:
            self.successors_of[node] = set()

    def __add_edge(self, edge: tuple[[int, int], int]):
        self.weighted_edges.add(edge)

        ((pred, suc), w) = edge
        self.__add_node(pred)
        self.__add_node(suc)
        self.__add_predecessor_of(suc, pred)
        self.__add_successors_of(pred, suc)

    def __add_predecessor_of(self, node: int, pred: int):
        if node not in self.predecessors_of:
            self.predecessors_of[node] = set()
        self.predecessors_of[node].add(pred)

    def __add_successors_of(self, node: int, suc: int):
        if node not in self.predecessors_of:
            self.successors_of[node] = set()
        self.successors_of[node].add(suc)