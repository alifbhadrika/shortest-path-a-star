import graph
import math

def test():
    G2 = graph.parseFile("dago.txt")
    G2.printGraph()
    for i in range (G2.numVertices):
        for j in range (G2.numVertices):
            print("{:4f}".format(G2.adj[i][j]), end=" ")
        print()

    # visualize graph tanpa path
    G2.visualize()

def start():
    print("#### A* Shortest Path Finder ####")
    filename = input("ENTER MAP NAME: ")
    G = graph.parseFile(filename)

    G.visualize() 

    nodes = [node for node in G.vertices]
    print("\nPLACES AT",filename.upper())
    for i in range (len(nodes)):
        print("[",i+1,"]", nodes[i].name)

    src = int(input("SOURCE: "))
    dest = int(input("DESTINATION: "))

    out = G.computeAStar(nodes[src-1].name,nodes[dest-1].name)
    if len(out[1]) == 0:
        print("THERE'S NO WAY YOU CAN GO FROM ", nodes[src-1].name," TO ",nodes[dest-1].name)
        print()
    else:
        print("\nTHE SHORTEST PATH FROM ", nodes[src-1].name," TO ",nodes[dest-1].name)
        for i in range (len(out[1])):
            if i == (len(out[1]) - 1):
                print(out[1][i])
            else:
                print(out[1][i], end=" --> ")
        print("\nWITH DISTANCE {:.3f} KMs\n".format(out[0]/1000))
        G.visualize(out[1]) 

if __name__ == '__main__':
    start()