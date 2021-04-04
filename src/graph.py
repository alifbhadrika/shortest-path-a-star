'''
Tugas Kecil 3 IF2211 Strategi Algoritma : Shortest Path with A* Algorithm
Cr : Mohammad Sheva Almeyda Sofjan (13519018/K01) | Alif Bhadrika Parikesit (13519186/K04)
'''
import math
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# file util
def parseFile(filename):
    '''
    File Parser
    '''
    try:
        with open('../test/'+filename+".txt", "r") as file:
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
    except:
        print("File not Found. Exiting program . . .")
        sys.exit()

def minFIdx(list): 
    '''
    Search minimum f func index from a list
    '''
    min = 0
    for i in range(len(list)):
        if(list[i].f < list[min].f):
            min = i
    return min

class Vertex:
    def __init__(self, _name, _lat, _long):
        self.name = _name
        self.lat = _lat # Latitude
        self.long = _long # Longitude
        self.coorX = 6371 * math.cos(_lat) * math.cos(_long)
        self.coorY = 6371 * math.cos(_lat) * math.sin(_long)
        self.f = 0  #Estimated total cost of path from self to dst
        self.g = 0 # cost so far to reach self
        self.h = 0 # estimated cost from self to goal
        self.parent = None

    def printInfo(self):
        print(self.name,"Coordinate : (",self.lat,", ",self.long,") : Cartesian (",self.coorX,", ",self.coorY)

class Graph:
    def __init__(self, _numVertices):
        '''
        Constructor
        '''
        self.numVertices = _numVertices
        self.vertices = []
        self.adj = [[0 for i in range(_numVertices)] for j in range(_numVertices)]
    
    def addVertex(self, _name, _lat, _long):
        '''
        Vertex Adder
        '''
        newVertex = Vertex(_name, _lat, _long)
        self.vertices.append(newVertex)

    def addEdge(self, v1, v2): 
        '''
        Edge adder
        '''
        idx1 = self.findVertexIdx(v1)
        idx2 = self.findVertexIdx(v2)
        self.adj[idx1][idx2] = self.calcDist(v1,v2)

    def syncAdj(self,adjmat):
        '''
        update adj matrix
        '''
        self.adj = adjmat

    def findVertexByIdx(self, idx): 
        '''
        search vertex by idx , return its name
        '''
        return self.vertices[idx].name
    
    def findVertexIdx(self, _name):
        '''
        search vertex idx by name, return its idx
        '''
        for i in range (self.numVertices):
            if (self.vertices[i].name == _name):
                return i
        return -1

    def findIdxByVertex(self,V): 
        '''
        search vertex idx by vertex, return its idx
        '''
        for i in range(self.numVertices):
            if(self.vertices[i].name == V.name):
                return i
        return -1
    def printGraph(self): 
        '''
        print graph
        '''
        for i in range(self.numVertices):
            self.vertices[i].printInfo()

    def calcDist(self,srcName,dstName): 
        '''
        passer to haverDist
        '''
        src = self.vertices[self.findVertexIdx(srcName)]
        dst = self.vertices[self.findVertexIdx(dstName)]
        return self.haverDist(src,dst)

    def haverDist(self,src,dst): 
        '''
        in m , haversine, calculate heuristic distance between two points
        '''
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
        '''
        Generate successor(neighbor) node of current node
        '''
        succNode = []
        for i in range(self.numVertices):
            if(self.adj[self.findIdxByVertex(current)][i] and i!=self.findIdxByVertex(current)):
                succNode.append(self.vertices[i])
        return succNode

    def computeAStar(self,srcName,dstName): 
        '''
        Compute Distance between two nodes using A* Algo
        '''
        if(self.findVertexIdx(srcName)==-1 or self.findVertexIdx(dstName)==-1 ): # Exit if node not found
            return []
        src = self.vertices[self.findVertexIdx(srcName)]  # src node
        dst = self.vertices[self.findVertexIdx(dstName)]  # dst node
        
        openList =[] # visited node + not expanded (queue node)
        closedList =[] # visited + expanded node
        for i in range(self.numVertices): # init h distance
            self.vertices[i].h = self.haverDist(self.vertices[i],dst)
        src.f = src.h
        openList.append(src) # init
        emp = False # openlist emptiness indicator
        while(not emp): 
            for i in range(self.numVertices): # Calculate f estimation in each iteration / hitung nilai f di tiap iterasi
                self.vertices[i].f = self.vertices[i].g + self.vertices[i].h
            currIdx = minFIdx(openList) 
            currNode = openList[currIdx] # currentNode is node in the openList which f value is lowest / node yang nilai f nya terendah

            if(currNode == dst): # found dest node, return result
                pathList = []
                currentNode = currNode
                while currentNode is not None:
                    pathList.append(currentNode.name)
                    currentNode = currentNode.parent
                return currNode.f,pathList[::-1]
            
            openList.remove(currNode) # remove currNode from openList (queue)
            succList = self.generateSucc(currNode) # Generate successor node list
            for succNode in succList: # foreach successor node
                tempCost = currNode.g + self.haverDist(currNode,succNode) # calculate temporary g value
                if(succNode in openList): 
                    if(succNode.g <= tempCost):
                        continue # continue to next iteration (current successsor node path is least cost path) / ke iterasi selanjutnya, current cost sudah lowest so far
                
                elif(succNode in closedList):
                    if(succNode.g <= tempCost):
                        continue # continue to next iteration (current successsor node path is least cost path)
                    
                    closedList.remove(succNode) # else remove from closedlist, add to queue (openlist) 
                    openList.append(succNode) # because current path is not the best one / karena tempCost lebih rendah dari current path(succ) g value
                else:
                    openList.append(succNode) # not in both, append to queue
                
                succNode.g = tempCost # sync g value if not continue
                succNode.parent = currNode  # append currNode to succNode parent (for path later on) 

            closedList.append(currNode) # finished exploring currNode
            if(len(openList)==0): # end condition
                emp = True

        if(currNode != dst): # path not found
            return []

    def visualize(self, aStarPath = None): 
        '''
        for visualizing graph
        '''
        if aStarPath is None:
            path = []
        else:
            path = aStarPath
        Gr = nx.Graph()
        for i in range (self.numVertices): # Initial Node+edge adder
            for j in range (self.numVertices):
                if (i<j):
                    if self.vertices[i].name not in Gr.nodes():
                        Gr.add_node(self.vertices[i].name, pos = (self.vertices[i].coorX, self.vertices[i].coorY))
                    if self.vertices[j].name not in Gr.nodes():
                        Gr.add_node(self.vertices[j].name, pos = (self.vertices[j].coorX, self.vertices[j].coorY))
                    if (self.adj[i][j] != 0):
                        formatted_weight = "{:.3f}".format(self.adj[i][j]/1000)
                        Gr.add_edge(self.vertices[i].name, self.vertices[j].name, weight = formatted_weight, relation = 'notinPath')
                else:
                    continue

        if(aStarPath is not None) : # Edge coloring
            for i in range(len(path) - 1):
                f_weight = "{:.3f}".format(self.adj[i][i+1]/1000)
                Gr.add_edge(path[i],path[i+1],weight = f_weight,relation = 'inPath')

        
        edge_color = {'inPath' : 'red', 'notinPath' : 'blue'}
        node_color = []
        for node in Gr.nodes():
            if node in path:
                node_color.append('red')
            else: 
                node_color.append('blue')

        weight = nx.get_edge_attributes(Gr, 'weight')
        pos = nx.get_node_attributes(Gr, 'pos')
        relation = nx.get_edge_attributes(Gr, 'relation')

        nx.draw_networkx(Gr, pos, node_color = node_color, edge_color=[edge_color[x] for x in relation.values()])
        nx.draw_networkx_edge_labels(Gr, pos, edge_labels = weight)
        plt.show()
            




        
