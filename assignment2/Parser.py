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
        
        #print(allNodes)
        #z=0
        for d in range(arcsStart+1, len(cleanLines)-1):
            
            lenPerson = len(cleanLines[d].split(" <-> ")[0])
            lenFriend = len(cleanLines[d].split(" <-> ")[1])
            person = cleanLines[d][:lenPerson]
            friend = cleanLines[d][-lenFriend:]
            personNode = Node(person)
            friendNode = Node(friend)
            newGraph.addNode(personNode,[friendNode])
            #newGraph.addNode(friendNode,[personNode])
            #print(person)
            #print(friend)

        print(allNodes)
        print(newGraph.nodes)
        for key, value in newGraph.nodes.items():
            print(key)
            """if key not in allNodes:
                newNode = Node(key)
                newGraph.addNode(newNode, [])"""
        #print(newGraph.nodes)

        """
            lenPerson = len(cleanLines[d].split(" <-> ")[0])
            lenFriend = len(cleanLines[d].split(" <-> ")[1])
            person = cleanLines[d][:lenPerson]
            friend = cleanLines[d][-lenFriend:]
            if allNodes[z]==person:
                personNode = Node(person)
                friendNode = Node(friend)
                newGraph.addNode(personNode,[friendNode])
                newGraph.addNode(friendNode,[personNode])
                z+=1
            elif allNodes[z]==friend:
                personNode = Node(person)
                friendNode = Node(friend)
                newGraph.addNode(friendNode,[personNode])
                newGraph.addNode(personNode,[friendNode])
                z+=1        
        return newGraph
        """
        return newGraph
                
parser = Parser()
graph = parser.importGraphTSV("graph.tsv")

#print(graph.nodes) #Alt er som det skal, men får ikke ut node n11 
#print(graph.edges) 


"""for i in graph.edges:
    for j in i.getEdge():
        print(j.getName())
    print("\n")

"""