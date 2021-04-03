class Vertex:
    def __init__(self, _name, _x, _y):
        self.name = _name
        self.x = x
        self.y = y

class Graph:
    def __init__(self, _numVertices):
        self.numVertices = _numVertices
        self.vertices = []
        self.adj = [[0 for i in range(_numVertices)] for j in range(_numVertices)]
    
    def addVertex(self, _name, _x, _y):
        newVertex = Vertex(_name, _x, _y)
        self.vertices.append(newVertex)
    
    def findVertexIdx(self, _name):
        for i in range (self.numVertices):
            if (vertices[i].name == _name):
                return i
        return -1
    
    #def findVertexFromIdx(self, )
    #belum selesai gue harus jenguk temen dulu

        