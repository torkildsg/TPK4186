"""" Group 14: Eivind Stangebye Larsen & Torkild Sandnes Grøstad """

from Graph import Graph
from Edge import Edge
from Node import Node


class Calculator: 

    """ Task 4 """
    # Q: A specific node or all nodes?
    def degreeOfNodes(self, graph):

        degreeDict = dict()
        nodes = graph.getNodes()

        for node in nodes: 
            #


""" Testing task 4 """
grid32 = Graph("Grid32")
n11 = Node("n11")
n12 = Node("n12")
n21 = Node("n21")
n22 = Node("n22")
n31 = Node("n31")
n32 = Node("n32")
grid32.addNode(n11, [n12, n21])
grid32.addNode(n12, [n22])
grid32.addNode(n21, [n22, n31])
grid32.addNode(n22, [n32])
grid32.addNode(n31, [n32])
grid32.addNode(n32, [])

print(list(grid32.getNodes()))
print(list())