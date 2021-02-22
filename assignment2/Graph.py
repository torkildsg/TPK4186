
class Graph():

    def __init__(self):
        self.nodes = dict()
        self.edges = []
    
    def addNode(self, nodeName):
        newNode = Node(nodeName)
        thisNodesEdges = newNode.getEdgeList()
        self.edges.append(thisNodesEdges)
        self.nodes[nodeName] = thisNodesEdges
