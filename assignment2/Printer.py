"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Graph import Graph
from Node import Node
from Edge import Edge

""" Task 2 """

class Printer:

    def printGraphTSV(self, graph):

        nodeList = graph.getNodes()
        arcList = [edge.getEdge() for edge in graph.getEdges()]
        nodeString = ""
        arcString = ""

        file = open('graph.tsv', 'w')
        file.write("graph " + graph.getName())
        file.write("\nnodes\n")

        if len(nodeList) > 3 and len(nodeList) % 2 == 0:
            for i in range(0, len(nodeList)-3, 2):
                nodeString += "  " + list(nodeList)[i] + ", " + list(nodeList)[i+1] + ",\n"
            nodeString += "  " + list(nodeList)[len(nodeList)-2] + ", " + list(nodeList)[len(nodeList)-1] + ";"
            file.write(nodeString)
        
        elif len(nodeList) > 3 and len(nodeList) % 2 != 0:
            for i in range(0, len(nodeList)-2, 2):
                nodeString += "  " + list(nodeList)[i] + ", " + list(nodeList)[i+1] + ",\n"
            nodeString += "  " + list(nodeList)[len(nodeList)-1] + ";"
            file.write(nodeString)

        elif len(nodeList) == 3: 
            file.write("  " + list(nodeList)[0] + ", " + list(nodeList)[1] + ",")
            file.write("  " + list(nodeList)[2] + ";")
        
        elif len(nodeList) == 2:
            file.write("  " + list(nodeList)[0] + ", " + list(nodeList)[1] + ";")

        elif len(nodeList) == 1:
            file.write("  " + list(nodeList)[0] + ";")

        file.write("\narcs\n")

        """ Denne må valideres for antall noder """
        for x in range(0, len(arcList)-1, 3):
                arcString += "  " + str(arcList[x][0].getName()) + " <-> " + str(arcList[x][1].getName()) + "," +\
                    "  " + str(arcList[x+1][0].getName()) + " <-> " + str(arcList[x+1][1].getName()) + "," +\
                        "  " + str(arcList[x+2][0].getName()) + " <-> " + str(arcList[x+2][1].getName()) + ",\n" 
        arcString += "  " + str(arcList[len(arcList)-1][0].getName()) + " <-> " + str(arcList[len(arcList)-1][1].getName()) + ";"
        
        file.write(arcString)
        file.write("\nend")        
        
""" Testing Task 2 """
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

#printer = Printer()
#printer.printGraphTSV(grid32)
