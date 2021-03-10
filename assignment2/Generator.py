"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Graph import Graph
from Edge import Edge
from Node import Node
from Calculator import Calculator
import random

class Generator:

    """ Task 11 """
    def getR(self):
        return random.uniform(0, 1)

    def barabasiAlbert(self, numberOfNodes):
        graph = Graph("Graph")
        n1 = Node("n1")
        n2 = Node("n2")
        graph.addNode(n1, [n2])
        graph.addNode(n2, [n1])
        i = 3
        nodeProb = dict()
        calc = Calculator()

        while i <= numberOfNodes:
            for key, value in graph.getNodes().items():
                nodeProb[value] = calc.getProbability(graph, value)
            newNodeName = "n" + str(i)
            newNode = Node(newNodeName)
            for key, value in nodeProb.items():
                if self.getR() < value:
                    graph.addNode(newNode, [key])
                    graph.addNode(key, [newNode])
                else:
                    continue
            i+=1
        return graph

""" Testing task 11 """
gen = Generator()

