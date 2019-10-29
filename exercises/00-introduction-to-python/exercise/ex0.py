class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.degree = self.count_degree()

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

    @staticmethod
    def read_graph():
        f = open("C:\\Users\\herta\\PycharmProjects\\Course-Knowledge-Graphs\\exercises\\00-introduction-to-python\\data\\01-triangle.txt")
        edges = [line.strip('\n').split() for line in f]
        nodes = int(edges.pop(0).pop())
        return Graph(nodes, edges)


graph = Graph.read_graph()
print(graph.degree)
graph.get_node_with_max_degree()
graph.get_node_with_min_degree()
