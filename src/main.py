import graph
import math
G = graph.Graph(2)
G.addVertex("Nitra",-6.1699203243112235, 106.63304752308868) #lat long
G.addVertex("ITB",-6.890713024901236, 107.61095946421104)
G.printGraph()
print(G.calcDist("Nitra","ITB"),"m")