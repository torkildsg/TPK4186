"""" Group 14: Eivind Stangebye Larsen & Torkild Sandnes Grøstad """

from Node import Node
from Edge import Edge
from Node import Node

class Graph:

    def __init__(self, name):
        self.nodes = dict()
        self.edges = [] # List of Edge-objects
        self.name = name

    def getNodes(self):
        return self.nodes
    
    def getEdges(self):
        return self.edges
    
    def getName(self):
        return self.name

    def edgeExist(self, node1, node2):
        for i in self.edges:
            if (i.getEdge()[0].getName() == node1.getName() and i.getEdge()[1].getName() == node2.getName()) or (i.getEdge()[0].getName() == node2.getName() and i.getEdge()[1].getName() == node1.getName()):
                return True
            else:
                return False

    # Legge til en addEdge?

    def addNode(self, node, friendNodes): # friendNodes er en liste med Node-objekter som allerede eksisterer

        if not friendNodes:
            self.nodes[node.getName()] = node
        else:
            for friend in friendNodes:
                if not self.edgeExist(node, friend):
                    newEdge = Edge(node, friend)
                    node.addEdge(newEdge)
                    friend.addEdge(newEdge)
                    self.edges.append(newEdge)
                self.nodes[node.getName()] = node

    def deleteNode(self, node):
        for edge in self.edges:
            if node in edge.getEdge():
                self.edges.remove(edge)
        del self.nodes[node.getName()]
    
    def deleteEdge(self, node1, node2):
        for edge in self.edges:
            if edge.getEdge() == [node1, node2] or edge.getEdge().reverse() == [node1, node2]:
                self.edges.remove(edge)
        

""" Testing Task 1 """
venner = Graph("venner")
eivind = Node("Eivind")
torkild = Node("Torkild")
venner.addNode(eivind, [torkild])
venner.addNode(torkild, [eivind])

#print(venner.nodes)
#print(venner.edges)




