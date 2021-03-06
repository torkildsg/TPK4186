"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Node import Node
from Edge import Edge
from Node import Node
from collections import defaultdict

class Graph:

    def __init__(self, name):
        self.nodes = dict() # Will look like this: {'nodeName': <nodeObject>, 'nodeName_2': <nodeObject_2>, ..., 'nodeName_k': <nodeObject_k>}
        self.edges = [] # List of Edge-objects
        self.name = name

    def getNodes(self):
        return self.nodes
    
    def getEdges(self):
        return self.edges
    
    def getName(self):
        return self.name

    def edgeExist(self, node1, node2):
        return any(edge.getEdge() == [node1, node2] or edge.getEdge() == [node2, node1] for edge in self.edges)

    """ Auxiliary function for Task 9 """
    def buildGraph(self): 
        edgeNodes = []
        for edge in self.edges:
            edgeNodes.append(edge.getEdge())
        graph = defaultdict(list)
        for edge in edgeNodes:
            i, j = edge[0].getName(), edge[1].getName()
            graph[i].append(j)
            graph[j].append(i)
        return dict(graph)

    def addNode(self, node, friendNodes): # friendNodes er en liste med Node-objekter som allerede eksisterer

        if node in self.nodes.values():
            if not friendNodes:
                print("The node '" + node.getName() + "' already exists.")
            else:
                for friend in friendNodes:
                    if self.edgeExist(node, friend):
                        continue
                    else:
                        if friend not in self.nodes.values():
                            self.nodes[friend.getName()] = friend
                        newEdge = Edge(node, friend)
                        node.addEdge(newEdge)
                        friend.addEdge(newEdge)
                        self.edges.append(newEdge)
        else:
            if not friendNodes:
                self.nodes[node.getName()] = node
            else:
                self.nodes[node.getName()] = node
                for friend in friendNodes:
                    if self.edgeExist(node, friend):
                        continue
                    else:
                        newEdge = Edge(node, friend)
                        node.addEdge(newEdge)
                        friend.addEdge(newEdge)
                        self.edges.append(newEdge)
                    
    def deleteNode(self, node):
        for edge in self.edges:
            if node in edge.getEdge():
                self.edges.remove(edge)
        del self.nodes[node.getName()]
    
    def deleteEdge(self, node1, node2):
        for edge in self.edges:
            if edge.getEdge() == [node1, node2] or edge.getEdge().reverse() == [node1, node2]:
                self.edges.remove(edge)
        





