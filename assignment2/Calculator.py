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

    """ Task 5 """
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

    """ Task 6 """
    def extractComponentsOfNode(self, node):

        c = [] # List of connected components found
        k = set(node.getNeighbours())  # The neighbours of this node
    
        while k:
            n = k.pop()
            group = {n} 
            queue = [n]
    
            while queue:
                n = queue.pop(0) # Get the next item from queue
                neighbours = set(n.getNeighbours()) # Fetch the neighbors
                neighbours.difference_update(group)  # Remove the neighbors already visited
                k.difference_update(neighbours)  # Remove the remaining nodes from the global set
                group.update(neighbours) # Add them to the group of connected nodes.
                queue.extend(neighbours)  # Add them to the queue, so we visit them in the next iterations.
            c.append(group) # Add the group to the list of groups.
        return list(c[0])
    
    """ Task 7 """
    def extractComponentsOfGraph(self, graph):

        componentsOfGraph = [] # List of connected components found
        nodesInGraph = set(list(graph.getNodes().values())) # The neighbours of this node

        while nodesInGraph:
            n = list(nodesInGraph)[0]
            componentsOfNode = set(self.extractComponentsOfNode(n))
            componentsOfGraph.append(list(componentsOfNode))
            nodesInGraph -= componentsOfNode
        return componentsOfGraph

    """Task 8 
    def plotDegreeOfNodes():
    """


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
#calc.degreeOfNodes(grid32)

""" Testing task 5 """
#calc.plotDegreeOfNodes(grid32)

""" Testing task 6 """
#print(calc.extractComponentsOfNode(n11))
#for i in calc.extractComponentsOfNode(n11):
#    print(i.getName())

""" Testing task 7 """
grid70 = Graph("Grid70")
n11 = Node("n11")
n12 = Node("n12")
n21 = Node("n21")
n22 = Node("n22")
n31 = Node("n31")
n32 = Node("n32")
grid70.addNode(n11, [n12, n21])
grid70.addNode(n12, [n12, n21])
grid70.addNode(n21, [n12, n11])
grid70.addNode(n22, [n32, n31])
grid70.addNode(n31, [n22, n32])
grid70.addNode(n32, [n22, n31])

print(calc.extractComponentsOfGraph(grid70))