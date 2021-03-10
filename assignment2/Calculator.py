"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Graph import Graph
from Edge import Edge
from Node import Node
import matplotlib.pyplot as plt
import operator

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

    """ Part of task 11 """
    def sumOfDegrees(self, graph):
        thisDict = self.degreeOfNodes(graph)
        sum = 0
        for value in thisDict.items():
            sum += value[1]
        return sum
    
    def getProbability(self, graph, node):
        denominator = self.sumOfDegrees(graph)
        thisNodesEdge = node.getEdgeList()
        numerator = len(thisNodesEdge)
        fraction = float(numerator/denominator)
        return fraction

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

    """ Task 8 """ 
    def plotSizesOfConnectedComp(self, graph):

        compOfGraph = self.extractComponentsOfGraph(graph)
        labels = []
        degrees = []

        for count, i in enumerate(range(0, len(compOfGraph)), 1): # Start counting from 1
            labels.append('Subgraph #' + str(count))
            degrees.append(len(compOfGraph[i]))
       
        plt.scatter(labels, degrees) 
        plt.xlabel('Subgraph', fontsize=15)
        plt.ylabel('Size of subgraph', fontsize=15)
        plt.yticks([i for i in range(0, max(degrees)+2)])
        plt.grid()
        plt.show() 
    
    """ Task 9 """
    def shortestPathBFS(self, graph, start, goal): 
        explored = []  
        queue = [[start]] 
         
        if start == goal: 
            print("End") 
            return 

        while queue: 
            path = queue.pop(0) 
            node = path[-1] 
            
            if node not in explored: 
                neighbours = graph[node] 
                
                for neighbour in neighbours: 
                    newPath = list(path) 
                    newPath.append(neighbour) 
                    queue.append(newPath) 
                    
                    if neighbour == goal: 
                        return len(newPath)-1
                explored.append(node) 
        return False
    
    def distanceToAllNodes(self, graph, startNode):
        startNode = startNode.getName()
        dictGraph = graph.buildGraph()
        #print(dictGraph)
        nodesInGraph = [key[0] for key in graph.getNodes().items()]
        nodesInGraph.remove(startNode)
        distanceDict = dict()

        
        for node in nodesInGraph:
            length = self.shortestPathBFS(dictGraph, startNode, node)
            distanceDict[node] = length
        
        return distanceDict 
        
    """ Task 10 """
    def diameterOfGraph(self,graph):
        
        dictGraph = graph.buildGraph()
        combDict = dict()
        nodesInGraph = [key[1] for key in graph.getNodes().items()]
   
        for node in nodesInGraph:
            dictWithDistances = self.distanceToAllNodes(graph, node)
            for n in dictWithDistances:
                combDict[node.getName() + " -> "+ n] = str("Diameter: "+str(dictWithDistances[n]))
        return list(max(combDict.items(), key = operator.itemgetter(1)))

    
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
#print(calc.extractComponentsOfGraph(grid70))

""" Testing task 8 """
#calc.plotSizesOfConnectedComp(grid70)

""" Testing task 9"""
#print(calc.distanceToAllNodes(grid32, n11))

""" Testing task 10 """
#print(calc.diameterOfGraph(grid32))

""" Testing task 11 """
print(calc.getProbability(grid32, n11))