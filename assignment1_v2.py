"""" Group 14: Eivind Stangebye Larsen & Torkild Sandnes Grøstad """

import csv

""" Task 1 """

class Team:
    
    def __init__(self, name, trigram):
        self.info = [name, trigram, 0, 0, 0, 0, 0, 0, 0]

    # 2 = number of games won, 3 = number of games lost, 4 = number of games draw, 
    # 5 = total points, 6 = number of goals for, 7 = number of goals against, 8 = goaldifference
    
    def getName(self):
        return self.info[0]
    
    def setName(self, name):
        self.info[0] = name
    
    def getTrigram(self):
        return self.info[1]

    def setTrigram(self, trigram):
        if(len(trigram)>3):
            print("Trigram cant be more than three characters.")
        else:
            self.info[1] = trigram
    
    def setNumGamesWon(self, gamesWon):
        self.info[2] = gamesWon

    def getNumGamesWon(self):
        return self.info[2]
    
    def setNumGamesLost(self, gamesLost):
        self.info[3] = gamesLost
    
    def getNumGamesLost(self):
        return self.info[3]

    def setNumGamesDraw(self, gamesDraw):
        self.info[4] = gamesDraw
    
    def getNumGamesDraw(self):
        return self.info[4]
    
    def setTotalpoints(self, team):
        totalPoints = getNumGamesWon(team) * 3 + getNumGamesDraw(team) 
        self.info[5] = totalPoints

    def getTotalpoints(self):
        return self.info[5]
    
    def setNumOfGoalsFor(self, numOfGoalsFor):
        self.info[6] = numOfGoalsFor
    
    def getNumOfGoalsFor(self):
        return self.info[6]

    def setNumOfGoalsAgainst(self, numOfGoalsAgainst):
        self.info[7] = numOfGoalsAgainst

    def getNumOfGoalsAgainst(self):
        return self.info[7]

    def setGoalDifference(self, team):
        goalDifference = getNumOfGoalsFor(team) - getNumOfGoalsAgainst(team)
        self.info[8] = goalDifference

    def getGoalDifference(self):
        return self.info[8]
    
    """" Part one of Task 5. This is equivalent to 'Print_Team' """
    def __str__(self):
        return "Trigram: " + self.getTrigram() + "\nGames won: " + str(self.getNumGamesWon()) + \
            "\nGames draw: " + str(self.getNumGamesDraw()) + "\nGoals scored: " + str(self.getNumOfGoalsFor()) + \
            "\nGoals conceded: " + str(self.getNumOfGoalsAgainst()) + "\nPoints: " + str(self.getTotalpoints())



""" Task 2 """

class Game:

    def __init__(self, trigramHometeam, hometeamScore, trigramVisitorteam, visitorteamScore):
        self.gameInfo = [trigramHometeam, hometeamScore, trigramVisitorteam, visitorteamScore]
    
    def setTrigramHometeam(self, trigram):
        self.gameInfo[0] = trigram
    
    def getTrigramHometeam(self):
        return self.gameInfo[0]
    
    def setTrigramVisitorteam(self, trigram):
        self.gameInfo[2] = trigram
    
    def getTrigramVisitorteam(self):
        return self.gameInfo[2]
    
    def setScoreHometeam(self, hometeamScore):
        self.gameInfo[1] = hometeamScore

    def getScoreHometeam(self):
        return self.gameInfo[1]

    def setScoreVisitorteam(self, visitorteamScore):
        self.gameInfo[3] = visitorteamScore

    def getScoreVisitorteam(self):
        return self.gameInfo[3]
    

    """Part two of Task 5. 
    This is equivalent to 'Print_Game' 
    """
    def __str__(self):
        return self.getTrigramHometeam() + "           " + str(self.getScoreHometeam()) + \
            "             " + self.getTrigramVisitorteam() + "              " + str(self.getScoreVisitorteam())


    

""" Task 3 """

class Championship:

    def __init__(self):
        self.teams = dict() # vil se slik ut {"RBK" : [RBK, rosenborg], ...}
        self.games = [] # Inneholder Game-objekter, som igjen inneholder en liste. Må bruke Game gettere og settere for å aksessere


    def lookForTeam(self, trigram):
        if(trigram in self.teams):
            return trigram
        else:
            return print("The team '" + trigram + "' does not participate in this championship.")

    def newTeam(self, name, trigram):
        newTeam = Team(name, trigram) # Kaller på Team-klassen
        self.teams[trigram] = newTeam 

    def getTeams(self):
        return self.teams
    
    def newGame(self, trigramHometeam, hometeamScore, trigramVisitorteam, visitorteamScore):
        newGame = Game(trigramHometeam, hometeamScore, trigramVisitorteam, visitorteamScore)
        self.games.append(newGame)
    
    def getGames(self):
        return self.games
    
    
    """Part three of task 5. 
    This is equivalent with the 'Print_ChampionshipDescription'. 
    Prints all information associated with a championship"""

    def __str__(self):
        print("#Name"+" "+"Code".rjust(25))

        for team in self.teams:
            print(self.teams[team].getName() + " " + self.teams[team].getTrigram().rjust(30-len(self.teams[team].getName())))
        
        print("\n#Home code"+ "    " + "Home score" + "    " + "#Visitor code" + "    " + "Visitor score")

        for game in self.games:
            print(game)


        return '' # Innebygde metoden sier at man må returnere en innebygd string. Omgår dette ved å sette denne

    """ Task 6 """

    def importChampionship(self, fileName):
        try:
            inputFile = open(fileName, "r")
        except:
            return "The file " + fileName + " does not exist."
        
        read_tsv = csv.reader(inputFile, delimiter="\t")

        for row in read_tsv:
            if (len(row)==2) and (row[0] != "#Name"):
                
            elif (len(row)==4) and (row[0] != "#Home code"):
                  
            return 

        inputFile.close()


""" Task 4 """
cup = Championship()
cup.newTeam("Odd ballklubb", "ODD")
cup.newTeam("Rosenborg ballklubb", "RBK")
cup.newTeam("Lyn FK", "LYN")
cup.newGame("LYN", 2, "RBK", 1)
cup.newGame("RBK", 1, "ODD", 4)
cup.newGame("ODD", 3, "LYN", 2)
print(cup.getGames()) # Kan se i terminalen at tre game-objekter er opprettet



print(cup)