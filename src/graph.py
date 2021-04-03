import math
class Vertex:
    def __init__(self, _name, _lat, _long):
        self.name = _name
        self.lat = _lat
        self.long = _long
        self.f = 0
        self.g = 0
        self.h = 0
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
        idx2 = self.findVertexIdx(v1)
        self.adj[idx1][idx2] = self.calcDist(v1, v2)
        
    def syncAdj(self,adjmat):
        self.adj = adjmat

    def findVertexByIdx(self, idx):
        return self.vertices[idx].name

    def findVertexIdx(self, _name):
        for i in range (self.numVertices):
            if (self.vertices[i].name == _name):
                return i
        return -1
    def printGraph(self):
        for i in range(self.numVertices):
            self.vertices[i].printInfo()

    def calcDist(self,srcName,dstName): # in m , haversine
        src = self.vertices[self.findVertexIdx(srcName)]
        dst = self.vertices[self.findVertexIdx(dstName)]
        lat1 = math.radians(src.lat)
        lat2 = math.radians(dst.lat)
        long1 = math.radians(src.long)
        long2 = math.radians(dst.long)
        deltaLat = lat2 - lat1
        deltaLong= long2 - long1
        a = (math.sin(deltaLat/2))**2 + math.cos(lat1)*math.cos(lat2)*(math.sin(deltaLong/2))**2
        c = 2 * math.asin(math.sqrt(a))
        return 6371 * c * 1000

# file util
def parseFile(filename):
    with open('test/'+filename, "r") as file:
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