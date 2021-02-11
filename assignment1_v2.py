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
        self.info[2] += gamesWon

    def getNumGamesWon(self):
        return self.info[2]
    
    def setNumGamesLost(self, gamesLost):
        self.info[3] += gamesLost
    
    def getNumGamesLost(self):
        return self.info[3]

    def setNumGamesDraw(self, gamesDraw):
        self.info[4] += gamesDraw
    
    def getNumGamesDraw(self):
        return self.info[4]
    
    def setTotalpoints(self):
        totalPoints = self.getNumGamesWon() * 3 + self.getNumGamesDraw() 
        self.info[5] = totalPoints

    def getTotalpoints(self):
        return self.info[5]
    
    def setNumOfGoalsFor(self, numOfGoalsFor):
        self.info[6] += numOfGoalsFor
    
    def getNumOfGoalsFor(self):
        return self.info[6]

    def setNumOfGoalsAgainst(self, numOfGoalsAgainst):
        self.info[7] += numOfGoalsAgainst

    def getNumOfGoalsAgainst(self):
        return self.info[7]

    def setGoalDifference(self):
        goalDifference = self.getNumOfGoalsFor() - self.getNumOfGoalsAgainst()
        self.info[8] = goalDifference

    def getGoalDifference(self):
        return self.info[8]
    
    """" Part one of Task 5. This is equivalent to 'Print_Team' """

    def __str__(self):
        f = open('teamFile.csv','w')
        f.write( "Trigram: " + self.getTrigram() + "\nGames won: " + str(self.getNumGamesWon()) + \
            "\nGames draw: " + str(self.getNumGamesDraw()) + "\nGoals scored: " + str(self.getNumOfGoalsFor()) + \
            "\nGoals conceded: " + str(self.getNumOfGoalsAgainst()) + "\nPoints: " + str(self.getTotalpoints()))
        f.close()

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
    
    """ Task 12"""

    def pointHomeTeams(self): 
        homeTeamGoals = self.getScoreHometeam()
        visitorTeamGoals = self.getScoreVisitorteam()
        if homeTeamGoals > visitorTeamGoals:
            return 3
        elif homeTeamGoals == visitorTeamGoals:
            return 1
        else: return 0
    
    def pointVisitorTeams(self): 
        homeTeamGoals = self.getScoreHometeam()
        visitorTeamGoals = self.getScoreVisitorteam()
        if homeTeamGoals < visitorTeamGoals:
            return 3
        elif homeTeamGoals == visitorTeamGoals:
            return 1
        else: return 0

    
    """ Task 12 done"""
    

    """Part two of Task 5. - This is equivalent to 'Print_Game' 
    """
    def __str__(self):
        f = open('gameFile.csv','w')
        f.write(self.getTrigramHometeam() + "           " + str(self.getScoreHometeam()) + \
            "             " + self.getTrigramVisitorteam() + "              " + str(self.getScoreVisitorteam()))
        f.close()


    

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

        f = open('championshipFile.csv','w')

        
        

        f.write("#Name"+" "+"Code".rjust(25)+"\n")

        for team in self.teams:
            f.write(self.teams[team].getName() + " " + self.teams[team].getTrigram().rjust(30-len(self.teams[team].getName()))+"\n")
        
        f.write("\n"+"#Home code"+ "    " + "Home score" + "    " + "#Visitor code" + "    " + "Visitor score")

        for game in self.games:
            f.write("\n"+str(game))

        f.close()

        return '' # Innebygde metoden sier at man må returnere en innebygd string. Omgår dette ved å sette denne

    """ Task 6 """

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
    
    """Task 7"""

    def UpdateStatistics(self):
        for game in self.games:
            trigramHometeam = game.getTrigramHometeam()
            trigramVisitorteam = game.getTrigramVisitorteam()

            scoreHometeam = game.getScoreHometeam()
            scoreVisitorteam = game.getScoreVisitorteam()

            homeTeam = self.teams[trigramHometeam]
            visitorTeam = self.teams[trigramVisitorteam]

            #-----Update games drawn,lost & won
            if scoreHometeam > scoreVisitorteam:
                homeTeam.setNumGamesWon(1)
                visitorTeam.setNumGamesLost(1)

            elif scoreHometeam == scoreVisitorteam:
                homeTeam.setNumGamesDraw(1)
                visitorTeam.setNumGamesDraw(1)

            elif scoreHometeam < scoreVisitorteam:
                visitorTeam.setNumGamesWon(1)
                homeTeam.setNumGamesLost(1)

            #----- Update total points
            homeTeam.setTotalpoints()
            visitorTeam.setTotalpoints()

            #--- Update goals scored, consided & goaldifference
            homeTeam.setNumOfGoalsFor(scoreHometeam)
            visitorTeam.setNumOfGoalsFor(scoreVisitorteam)
            homeTeam.setNumOfGoalsAgainst(scoreVisitorteam)
            visitorTeam.setNumOfGoalsAgainst(scoreHometeam)
            homeTeam.setGoalDifference()
            visitorTeam.setGoalDifference()
           

    """ Task 8 """

    def getRanking(self): #Må få inn at den sorterer på målforskjell dersom likt antall poeng

        newList = []
        for team in self.teams:
            newList.append([self.teams[team].getTrigram(), self.teams[team].getTotalpoints()])
        sortedList = sorted(newList, key=lambda l:l[1], reverse=True) 
        return sortedList

    """Task 9"""

    def printRanking(self):
        
        print("Pos".ljust(7) + "Team".ljust(30) + "Played".ljust(10) + "Wins".ljust(10) + "Draws".ljust(10) + \
            "Losses".ljust(10) + "Goals For".ljust(15) + "Goals Against".ljust(20) + "Goal Difference".ljust(20) + "Points")
        ranking = 1
        for team in self.getRanking():

            print(str(ranking).ljust(7) + self.teams[team[0]].getName().ljust(30) + str(self.teams[team[0]].getNumGamesDraw() + \
                self.teams[team[0]].getNumGamesLost() + self.teams[team[0]].getNumGamesWon()).ljust(10) + str(self.teams[team[0]].getNumGamesWon()).ljust(10) + \
                    str(self.teams[team[0]].getNumGamesDraw()).ljust(10) + str(self.teams[team[0]].getNumGamesLost()).ljust(10) + str(self.teams[team[0]].getNumOfGoalsFor()).ljust(15) + \
                        str(self.teams[team[0]].getNumOfGoalsAgainst()).ljust(20) + str(self.teams[team[0]].getGoalDifference()).ljust(20) + str(self.teams[team[0]].getTotalpoints()))

            ranking += 1

    """Task 10"""
    
    def updateGameLists(self):

        self.allGamesByTeams = dict()
        
        for team in self.teams:
            teamTrigram = self.teams[team].getTrigram()
            teamHomegames=[]
            teamVisitorgames =[]
            
            for game in self.getGames():
                if  teamTrigram == game.getTrigramHometeam():
                    teamHomegames.append(game)
                elif teamTrigram == game.getTrigramVisitorteam():
                    teamVisitorgames.append(game)

            teamgames = [teamHomegames,teamVisitorgames]

            self.allGamesByTeams[teamTrigram] = teamgames  

        return self.allGamesByTeams

    """" Task 11 """
    #Gjør denne

    
    """ Task 12 """

    def getRankingByHome(self):
        games = self.updateGameLists()
        homeranking = []
        for team in games:
            sum = 0
            for game in games[team][0]:
                sum += game.pointHomeTeams()
            
            homeranking.append([team, sum])
        
        sortedList = sorted(homeranking, key=lambda l:l[1], reverse=True) 
            
        return sortedList
    
    def getRankingByVisitor(self):
        games = self.updateGameLists()
        visitorRanking = []
        for team in games:
            sum = 0
            for game in games[team][0]:
                sum += game.pointVisitorTeams()
            
            visitorRanking.append([team, sum])
        
        sortedList = sorted(visitorRanking, key=lambda l:l[1], reverse=True) 
        return sortedList
            
    """ Task 13 """
    def rankingByGoalsFor(self):
        newList = []
        for team in self.teams:
            newList.append([self.teams[team].getTrigram(), self.teams[team].getNumOfGoalsFor()])
        sortedList = sorted(newList, key=lambda l:l[1], reverse=True) 
        return sortedList
    
    def rankingByGoalsAgainst(self):
        newList = []
        for team in self.teams:
            newList.append([self.teams[team].getTrigram(), self.teams[team].getNumOfGoalsAgainst()])
        sortedList = sorted(newList, key=lambda l:l[1], reverse=False) 
        return sortedList






        

    
    

""" Task 4 """
cup = Championship()
cup.newTeam("Odd ballklubb", "ODD")
cup.newTeam("Rosenborg ballklubb", "RBK")
cup.newTeam("Lyn FK", "LYN")
cup.newGame("LYN", 2, "RBK", 1)
cup.newGame("ODD", 9, "LYN", 1)
cup.newGame("RBK", 1, "ODD", 4)
cup.newGame("LYN", 1, "RBK", 4)
cup.newGame("ODD", 3, "LYN", 2)
#print(cup.getGames()) # Kan se i terminalen at tre game-objekter er opprettet

""" Testing 5 """
#print(cup)
#print()


""" Testing task 6 """
newChamp = Championship()
fileName = "PremierLeague2019-2020-Description.tsv"
newChamp.importChampionship(fileName)
#print(newChamp)

""" Testing task 7 """
cup.UpdateStatistics()
#print(cup.teams["LYN"])

""" Testing task 8 """
#cup.getRanking()


""" Test 9 """
#cup.printRanking()

"""Test 10"""
#cup.updateGameLists()
#print(cup.allGamesByTeams) #dictionary with Trigrams as keys. "RBK":[[Games where RBK plays at home],[Games where RBK plays as visitor]]

""" Test 11 """
#cup.printGameTable()

""" Test 12"""
#print(cup.getRanking()) #Task 8 (original)
#print(cup.getRankingByHome()) # considering only the games played at home
#print(cup.getRankingByVisitor()) # considering only the games played as visitors

#As we kan see, there is a big difference

""" Test 13 """
#print(cup.rankingByGoalsFor()) #prints trigram and number of goals for, where the first is the one with the most goals for
#print(cup.rankingByGoalsAgainst()) #prints trigram and number of goals agains, where the first is the one with the least goals against
