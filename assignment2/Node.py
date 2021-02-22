

class Node:

    def __init__(self, name):
        self.name = name
        self.edgeList = []
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def addEdge(self, edge):
        self.edgeList.append(edge)
    
    def getEdgeList(self):
        return self.edgeList
    
