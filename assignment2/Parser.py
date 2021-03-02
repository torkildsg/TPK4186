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
        content = inputFile.readlines()
        content = [x.strip() for x in content] 
        for i in content:
            if i not in ['arcs','nodes','end']:
                i = i.replace(';','')
                lines+=i.split(", ")
        #print(lines)
        

        nameOfGraph = lines[0][len('graph '):]
        newGraph = Graph(nameOfGraph)
        
        for e in lines:
            e =e.strip(",")
            e = e.strip()
            allNodes = []
            if (len(e) == 3):
                allNodes.append(e)
                #print(e)
                #Hver node

            elif (len(e)==11):
                person = e[:3]
                friend = e[-3:]
                
                #hver arcs 
                #print(person)
                #print(friend)
                if person not in allNodes:
                    personNode = Node(friend)
                    friendNode = Node(person)
                    newGraph.addNode(personNode,[friendNode])
                else:
                    personNode = Node(person)
                    friendNode = Node(friend)
                    newGraph.addNode(personNode,[friendNode])
                

        return newGraph
    
       
                
parser = Parser()
graph = parser.importGraphTSV("graph.tsv")
print(graph.nodes) #Alt er som det skal, men får ikke ut node n11 
print(graph.edges)



"""dictWithNodes = graph.getNodes()
for key,value in dictWithNodes.items():
    print(value.getEdgeList())"""
  



"""

    def importChampionship(self, fileName):
        try:
            inputFile = open(fileName, "r")
        except FileNotFoundError:
            print("The file " + fileName + " does not exist.")
        
        read_tsv = csv.reader(inputFile, delimiter="\t")

        for row in read_tsv:
            if (len(row)==2) and (row[0] != "#Name"):
                self.newTeam(row[0], row[1])
            elif (len(row)==4) and (row[0] != "#Home code"):
                  self.newGame(row[0], row[1], row[2], row[3])
        return self
        inputFile.close()

"""