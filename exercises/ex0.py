from exercises.DirectedGraph import *
from exercises.graph import *

print(open(triangle))
graph = DirectedGraph.from_file(triangle)
print(graph.degree)
# Exercise 0.3
graph.get_node_with_max_degree()
# Exercise 0.4

graph.get_node_with_min_degree()
