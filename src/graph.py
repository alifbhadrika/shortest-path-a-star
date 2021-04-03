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
    
    def findVertexIdx(self, _name):
        for i in range (self.numVertices):
            if (self.vertices[i].name == _name):
                return i
        return -1
    def printGraph(self):
        for i in range(self.numVertices):
            self.vertices[i].printInfo()

    def calcDist(self,srcName,dstName): # in km , haversine
        src = self.vertices[self.findVertexIdx(srcName)]
        dst = self.vertices[self.findVertexIdx(dstName)]
        lat1 = math.radians(src.lat)
        lat2 = math.radians(dst.lat)
        long1 = math.radians(src.long)
        long2 = math.radians(dst.long)
        deltaLat = math.radians(lat2 - lat1)
        deltaLong=math.radians(long2 - long1)
        a = math.sin(deltaLat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(deltaLong/2)**2
        c = 2 * math.asin(math.sqrt(a))
        return 6371 * c
        