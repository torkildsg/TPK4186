"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

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
        degrees = []

        for key, value in nodes.items():
            labels.append(key.getName())
            degrees.append(value)
        
        ticklabel_y = [i for i in range(0, len(labels))] 
  
        plt.scatter(labels, degrees) 
        plt.xlabel('Node', fontsize=15)
        plt.ylabel('Degree of node', fontsize=15)
        plt.yticks(ticklabel_y)
        plt.grid()
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
