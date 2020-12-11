from exercises.ex0 import Graph


class METISGraph:

    def __init__(self, graph):
        self.nodes = graph.nodes
        self.edges = len(graph.edges)
        self.neighbors = {}

        for edge in graph.edges:
            if edge[0] in self.neighbors:
                self.neighbors[edge[0]].add(edge[1])
            else:
                self.neighbors[edge[0]] = {edge[1]}

    def find_triangle(self):
        path = []
        for n0 in self.neighbors:
            for n1 in self.neighbors[n0]:
                for n2 in self.neighbors[n1]:
                    if n0 in self.neighbors[n2]:
                        path.append([n0, n1, n2])
        return path


graph = Graph.from_file()
graph = METISGraph(graph)
p = graph.find_triangle()
print(p)