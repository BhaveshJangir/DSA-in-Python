class Graph:
    def __init__(self,vno):
        self.NoOfVertex = vno
        self.addMatrix = [ [0]*vno for e in range(vno) ]

    def add_edge(self,u,v,weight=1):
        if 0<=u<self.NoOfVertex and 0<=v<self.NoOfVertex:
            self.addMatrix[u][v] = weight
            self.addMatrix[v][u] = weight
        else:
            print('Invalid edges')

    def remove_edge(self,u,v):
        if 0<=u<self.NoOfVertex and 0<=v<self.NoOfVertex:
            self.addMatrix[u][v] = 0
            self.addMatrix[v][u] = 0
        else:
            print('Invalid edges')

    def has_edge(self,u,v):
        return self.addMatrix[u][v] != 0

    def pEdges(self):
        for rowList in self.addMatrix:
            print(" ".join(map(str,rowList)))

g= Graph(5)
g.add_edge(0,1)
g.add_edge(3,4)
print(g.has_edge(3,4))
g.pEdges()
print()
g.remove_edge(3,4)
g.pEdges()