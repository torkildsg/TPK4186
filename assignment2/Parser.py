"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

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
        content = [x.strip().replace(';','') for x in inputFile.readlines()] 

        for i in content:
            lines += i.split(", ")

        for line in lines:
            line = line.replace(',','').strip()
            cleanLines.append(line)

        nameOfGraph = lines[0][len('graph '):]
        newGraph = Graph(nameOfGraph)
        nodeStart = cleanLines.index("nodes")
        arcsStart = cleanLines.index("arcs")
        
        for d in range(arcsStart+1, len(cleanLines)-1):
            lenPerson = len(cleanLines[d].split(" <-> ")[0])
            lenFriend = len(cleanLines[d].split(" <-> ")[1])
            person = cleanLines[d][:lenPerson]
            friend = cleanLines[d][-lenFriend:]

            personNode = Node(person)
            friendNode = Node(friend)

            newGraph.addNode(personNode,[friendNode])
            newGraph.addNode(friendNode,[personNode])       
        return newGraph
                


