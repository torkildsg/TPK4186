"""" Group 14: Eivind Stangebye Larsen & Torkild Sandnes Grøstad """

from Graph import Graph
from Edge import Edge
from Node import Node
import csv


class Parser:

    
    def importGraphTSV(self, fileName):

        try:
            inputFile = open(fileName, 'r')
        except FileNotFoundError:
            print("The file " + fileName + "does not exist.")
        
        lines = []
        cleanLines = []
        content = inputFile.readlines()
        content = [x.strip() for x in content] 
        for i in content:
            #print(i)
            i = i.replace(';','')
            lines+=i.split(", ") 
        
        for el in lines:
            el = el.replace(',','').strip()
            cleanLines.append(el)

        nameOfGraph = lines[0][len('graph '):]
        newGraph = Graph(nameOfGraph)
        allNodes = []

        nodeStart = cleanLines.index("nodes")
        arcsStart = cleanLines.index("arcs")

        for q in range(nodeStart+1,arcsStart):
            allNodes.append(cleanLines[q])
        
        for d in range(arcsStart+1, len(cleanLines)-1):
            print(cleanLines[d])
            lenPerson = len(cleanLines[d].split(" <-> ")[0])
            lenFriend = len(cleanLines[d].split(" <-> ")[1])
            person = cleanLines[d][:lenPerson]
            friend = cleanLines[d][-lenFriend:]
    
            personNode = Node(person)
            friendNode = Node(friend)

            newGraph.addNode(personNode,[friendNode])
            newGraph.addNode(friendNode,[personNode])
            
                                   
        
        #print(allNodes)
        return newGraph
              
parser = Parser()
graph = parser.importGraphTSV("graph.tsv")
print(graph.nodes) #Alt er som det skal, men får ikke ut node n11 
for i in graph.edges:
    print('\n')
    for j in i.getEdge():
        print(j.getName())

#print(graph.edges) 
