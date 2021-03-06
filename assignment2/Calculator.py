"""" Group 14: Eivind Stangebye Larsen & Torkild Sandnes Grøstad """

from Graph import Graph
from Edge import Edge
from Node import Node
import matplotlib.pyplot as plt

class Calculator: 

    """ Task 4 """
    # Q: A specific node or all nodes?
    def degreeOfNodes(self, graph):

        degreeDict = dict()
        nodes = graph.getNodes()
        
        for key, value in nodes.items():
            thisNode = value
            thisNodesEdges = thisNode.getEdgeList()
            degreeDict[thisNode] = len(thisNodesEdges)

        return degreeDict # Will look like this: {node_1: degreeOfNode, node_2: degreeOfNode, ..., node_k: degreeOfNode}

    def plotDegreeOfNodes(self, graph):

        nodes = self.degreeOfNodes(graph)
        labels = []
        sizes = []

        for key, value in nodes.items():
            labels.append(key.getName())
            sizes.append(value)

        explode = (0, 0, 0, 0, 0, 0)  
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, startangle=90)
        ax1.axis('equal')  
        plt.show()

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

calc = Calculator()
calc.degreeOfNodes(grid32)
calc.plotDegreeOfNodes(grid32)
