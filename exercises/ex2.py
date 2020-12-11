import gzip

class Graph:

    def __init__(self, triple):
        self.triple = triple

    #@staticmethod
    #def read():


path = "/data/dblp/authorship-snippet.nt.gz"
with gzip.open(path, 'rb') as file:
    print([line.strip('\n').split() for line in file])

