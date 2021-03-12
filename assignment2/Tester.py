"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Node import Node
from Edge import Edge
from Graph import Graph
from Printer import Printer
from Parser import Parser
from Calculator import Calculator
from Generator import Generator

""" Testing Task 1 """
venner = Graph("venner")
eivind = Node("Eivind")
torkild = Node("Torkild")
henrik = Node("Henrik")
tom = Node("Tom")
venner.addNode(eivind, [torkild])
venner.addNode(torkild, [eivind])
venner.addNode(henrik, [torkild, eivind])
venner.addNode(henrik, [tom, torkild])
"""
print(venner.nodes)
print(venner.edges)

# Deleting one node, and one edge
venner.deleteNode(tom)
venner.deleteEdge(henrik, eivind)
print(venner.nodes)
print(venner.edges)
"""


""" Testing task 2 """
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
"""printer = Printer()
printer.printGraphTSV(grid32)"""


""" Testing task 3 """
"""parser = Parser()
graph = parser.importGraphTSV("graph.tsv")
print(graph.nodes)
print(graph.edges)"""


""" Testing task 4 """
calc = Calculator()
"""print(calc.degreeOfNodes(grid32))"""


""" Testing task 5 """
"""calc.plotDegreeOfNodes(grid32)"""


""" Testing task 6 """
"""print(calc.extractComponentsOfNode(n11))
for i in calc.extractComponentsOfNode(n11):
    print(i.getName())"""


""" Testing task 7 """
grid70 = Graph("Grid70")  
n41 = Node("n41")
n42 = Node("n42")
n81 = Node("n81")
n82 = Node("n82")
n61 = Node("n61")
n62 = Node("n62")
grid70.addNode(n41, [n42, n81])
grid70.addNode(n42, [n41, n81])
grid70.addNode(n81, [n42, n41])
grid70.addNode(n82, [n62, n61])
grid70.addNode(n61, [n82, n62])
grid70.addNode(n62, [n82, n61])
"""print(calc.extractComponentsOfGraph(grid70))"""


""" Testing task 8 """
"""calc.plotSizesOfConnectedComp(grid70)"""


""" Testing task 9"""
"""print(calc.distanceToAllNodes(grid32, n11))"""


""" Testing task 10 """
"""print(calc.diameterOfGraph(grid32))"""


""" Testing task 11 """
generator = Generator()
graph = generator.barabasiAlbert(50) # 50 nodes


""" Task 12 (and test of Task 11) """

# Test printing and parsing of the generated network
"""printer = Printer()
printer.printGraphTSV(graph)"""

"""parser = Parser()
parsedGraph = parser.importGraphTSV('graph.tsv')
print("Number of nodes: " + str(len(parsedGraph.getNodes())))
print("Number of edges: " + str(len(parsedGraph.getEdges())))"""


# Test if the generated network is made of one single connected component
"""print("Number of connected components: " + str(len(calc.extractComponentsOfGraph(graph))))"""


# Test if you could extract and plot the distributions of the degree of nodes
"""print(calc.degreeOfNodes(graph))
calc.plotDegreeOfNodes(graph)
print("Number of nodes: " + str(len(graph.getNodes()))) # Here you can see the number of nodes in the graph
"""

# Test if you can calculate the diameter of the network
"""print(calc.diameterOfGraph(graph))"""

