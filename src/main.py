import graph
import math

def test():
    G2 = graph.parseFile("test2.txt")
    G2.printGraph()
    for i in range (G2.numVertices):
        for j in range (G2.numVertices):
            print("{:4f}".format(G2.adj[i][j]), end=" ")
        print()

    print(G2.calcDist("A","F"))
    out = G2.computeAStar("A","F")

    G2.visualize(out)

    print(out)
