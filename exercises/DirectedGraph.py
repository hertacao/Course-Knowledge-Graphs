class DirectedGraph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.degree = self.count_degree()

    @classmethod
    def from_file(cls, filestring):
        f = open(filestring)
        edges = [line.split() for line in f]
        print("edges")
        print(edges)
        nodes = int(edges.pop(0).pop())
        graph = cls(nodes, edges)
        return graph

    def count_degree(self):
        degree = {}
        for edge in self.edges:
            if edge[0] in degree:
                degree[edge[0]] += 1
            else:
                degree[edge[0]] = 1
        return degree

    def get_node_with_max_degree(self):
        for node in self.degree:
            if self.degree[node] == self.nodes - 1:
                print(node)

    def get_node_with_min_degree(self):
        for node in self.degree:
            if self.degree[node] == 0:
                print(node)
