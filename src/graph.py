import math
import networkx as nx
import matplotlib.pyplot as plt

# file util
def parseFile(filename):
    with open('../test/'+filename, "r") as file:
        lines = file.readlines()
        # get number of vertices from 1st line
        numVertices = int(lines[0].strip())
        G = Graph(numVertices)

        # construct every vertex from line 2
        for i in range(1, numVertices + 1):
            vertexArgs = lines[i].strip().split(" ")
            G.addVertex(vertexArgs[0], float(vertexArgs[1]), float(vertexArgs[2]))

        # construct every edges from adj matrix
        for i in range(numVertices + 1, len(lines)):
            elmt = lines[i].strip().split(" ")
            rowIdx = i - (numVertices + 1)
            for j in range(numVertices):
                if elmt[j] == '1':
                    G.addEdge(G.findVertexByIdx(rowIdx), G.findVertexByIdx(j))

    return G

def minFIdx(list): # Search minimum f func index from a list
    min = 0
    for i in range(len(list)):
        if(list[i].f < list[min].f):
            min = i
    return min

class Vertex:
    def __init__(self, _name, _lat, _long):
        self.name = _name
        self.lat = _lat
        self.long = _long
        self.f = 0  #Estimated total cost of path from self to dst
        self.g = 0 # cost so far to reach self
        self.h = 0 # estimated cost from self to goal
        self.parent = None

    def getX(self):
        x = 6371 * math.cos(self.lat) * math.cos(self.long)
        return x

    def getY(self):
        y = 6371 * math.cos(self.lat) * math.sin(self.long)
        return y
        
    def printInfo(self):
        print(self.name,"Coordinate : (",self.lat,", ",self.long,")")

class Graph:
    def __init__(self, _numVertices):
        self.numVertices = _numVertices
        self.vertices = []
        self.adj = [[0 for i in range(_numVertices)] for j in range(_numVertices)]
    
    def addVertex(self, _name, _lat, _long):
        newVertex = Vertex(_name, _lat, _long)
        self.vertices.append(newVertex)

    def addEdge(self, v1, v2):
        idx1 = self.findVertexIdx(v1)
        idx2 = self.findVertexIdx(v2)
        self.adj[idx1][idx2] = 1
    def syncAdj(self,adjmat):
        self.adj = adjmat

    def findVertexByIdx(self, idx):
        return self.vertices[idx].name
    
    def findVertexIdx(self, _name):
        for i in range (self.numVertices):
            if (self.vertices[i].name == _name):
                return i
        return -1

    def findIdxByVertex(self,V):
        for i in range(self.numVertices):
            if(self.vertices[i].name == V.name):
                return i
        return -1
    def printGraph(self):
        for i in range(self.numVertices):
            self.vertices[i].printInfo()

    def calcDist(self,srcName,dstName): # passer to haverDist
        src = self.vertices[self.findVertexIdx(srcName)]
        dst = self.vertices[self.findVertexIdx(dstName)]
        return self.haverDist(src,dst)

    def haverDist(self,src,dst): # in m , haversine
        lat1 = math.radians(src.lat)
        lat2 = math.radians(dst.lat)
        long1 = math.radians(src.long)
        long2 = math.radians(dst.long)
        deltaLat = lat2 - lat1
        deltaLong= long2 - long1
        a = (math.sin(deltaLat/2))**2 + math.cos(lat1)*math.cos(lat2)*(math.sin(deltaLong/2))**2
        c = 2 * math.asin(math.sqrt(a))
        return 6371 * c * 1000

    def generateSucc(self,current):
        succNode = []
        for i in range(self.numVertices):
            if(self.adj[self.findIdxByVertex(current)][i] and i!=self.findIdxByVertex(current)):
                succNode.append(self.vertices[i])
        return succNode

    def computeAStar(self,srcName,dstName):
        if(self.findVertexIdx(srcName)==-1 or self.findVertexIdx(dstName)==-1 ):
            return []
        src = self.vertices[self.findVertexIdx(srcName)]  # src node
        dst = self.vertices[self.findVertexIdx(dstName)]  # dst node
        
        openList =[] # visited node + not expanded (queue node)
        closedList =[] # visited + expanded node
        for i in range(self.numVertices): # init h distance
            self.vertices[i].h = self.haverDist(self.vertices[i],dst)
        src.f = src.h
        openList.append(src) # init
        emp = False
        while(not emp):
            for i in range(self.numVertices):
                self.vertices[i].f = self.vertices[i].g + self.vertices[i].h
            currIdx = minFIdx(openList)
            currNode = openList[currIdx]

            if(currNode == dst): # found dest node
                pathList = []
                currentNode = currNode
                while currentNode is not None:
                    pathList.append(currentNode.name)
                    currentNode = currentNode.parent
                return currNode.f,pathList[::-1]
            
            openList.remove(currNode)
            succList = self.generateSucc(currNode)
            for succNode in succList:
                tempCost = currNode.g + self.haverDist(currNode,succNode)
                if(succNode in openList):
                    if(succNode.g <= tempCost):
                        continue
                
                elif(succNode in closedList):
                    if(succNode.g <= tempCost):
                        continue
                    succNodeIdx = closedList.index(succNode)
                    closedList.remove(succNode)
                    openList.append(succNode)
                else:
                    openList.append(succNode)
                
                succNode.g = tempCost
                succNode.parent = currNode

            closedList.append(currNode)
            if(len(openList)==0):
                emp = True

        if(currNode != dst):
            return []

    def visualize(self, aStar):
        path = aStar[1]
        Gr = nx.Graph()
        for i in range (self.numVertices):
            for j in range (self.numVertices):
                if (i<j):
                    if (adj[i][j] != 0):
                        if self.vertices[i].name not in Gr.nodes():
                            Gr.add_node(self.vertices[i].name, pos=(self.vertices[i].getX, self.vertices[i].getY))
                        if self.vertices[j].name not in Gr.nodes():
                            Gr.add_node(self.vertices[j].name, pos=(self.vertices[j].getX, self.vertices[j].getY))
                        if (self.vertices[i].name, self.vertices[j].name) in path:
                            Gr.add_edge(self.vertices[i].name, self.vertices[j].name, self.adj[i][j], relation='inPath')
                        else:
                            Gr.add_edge(self.vertices[i].name, self.vertices[j].name, self.adj[i][j], relation='notinPath')
                else:
                    break

        edge_color = {'inPath' : 'blue', 'notinPath' : 'red'}
        weight = nx.get_edge_attributes(Gr, 'weight')
        pos = nx.get_node_attributes(Gr, 'pos')
        relation = nx.get_edge_attributes(Gr, 'relation')
        

        nx.draw_networkx(Gr, pos, edge_color=[edge_color[x] for x in relation.values()])
        nx.draw_networkx_edge_labels(Gr, pos, edge_labels = weight)
            




        
