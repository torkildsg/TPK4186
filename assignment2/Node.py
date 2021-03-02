"""" Group 14: Eivind Stangebye Larsen & Torkild Sandnes Grøstad """

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

    




