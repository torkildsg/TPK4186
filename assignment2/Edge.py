

class Edge(node1, node2):

    def __init__(self, edge, node1, node2):
        self.edge = [node1, node2]


    def setEdge(self, edge, node1, node2):
        self.edge = [node1, node2]
    
    def getEdge(self):
        return self.edge
    
    