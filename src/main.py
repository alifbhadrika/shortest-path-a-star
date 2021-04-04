import graph
import math

def test():
    G2 = graph.parseFile("test1.txt")
    G2.printGraph()
    for i in range (G2.numVertices):
        for j in range (G2.numVertices):
            print(G2.adj[i][j])

    print(G2.calcDist("Nitra","Sadikin"))
    out = G2.computeAStar("Nitra","Sadikin")

    print(out)
    G2.visualize(out)
