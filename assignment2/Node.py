"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Node:

    def __init__(self, name):
        self.name = name
        self.thisNodesEdges = []
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def addEdge(self, friendNode):
        self.thisNodesEdges.append([friendNode])

    def getEdgeList(self):
        return self.thisNodesEdges

    def getNeighbours(self):
        edges = self.getEdgeList()
        neighbours = []
        for i in range(0, len(edges)):
            node1 = edges[i][0].getEdge()[0]
            node2 = edges[i][0].getEdge()[1]
            if node1 != self:
                neighbours.append(node1)
            else:
                neighbours.append(node2)
        return neighbours


    

 

