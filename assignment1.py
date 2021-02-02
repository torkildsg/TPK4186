
def Team_New(name, trigram, gamesWon, gamesLost, gamesDraw, numberOfGoalsFor, numberOfGoalsAgainst):
    return [name, trigram, gamesWon, gamesLost, gamesDraw, numberOfGoalsFor, numberOfGoalsAgainst]

def Team_GetName(team):
    return team[0]

def Team_SetName(team, name):
    team[0] = name

def Team_SetTrigram(team, trigram):
    team[1] = trigram

def Team_GetTrigram(team):
    return team[1]

def Team_SetNumGamesWon(team, gamesWon):
        team[2] = gamesWon
    
def Team_getNumGamesWon(team):
    return team[2]

def Team_SetNumGamesLost(team, gamesLost):
    team[3] = gamesLost

def Team_getNumGamesDraw(team):
    return team[4]

def Team_SetNumGamesDraw(team, gamesDraw):
    team[4] = gamesDraw

def Team_TotalPoints(team):
    totalPoints = Team_getNumGamesWon(team) * 3 + Team_getNumGamesDraw(team) 
    return totalPoints

def Team_setNumberOfGoalsFor(team, numberOfGoalsFor):
    team[5] = numberOfGoalsFor

def Team_getNumberOfGoalsFor(team):
    return team[5]

def Team_setNumberOfGoalsAgainst(team, numberOfGoalsAgainst):
    team[6] = numberOfGoalsAgainst

def Team_getNumberOfGoalsAgainst(team):
    return team[6]

def Team_goalDifference(team):
    goalDifference = Team_getNumberOfGoalsFor(team) - Team_getNumberOfGoalsAgainst(team)
    return goalDifference


# Testing

rosenborg = Team_New("Rosenborg", "RBK", 0 , 0, 0, 0, 0)
Team_GetName(rosenborg)
Team_GetTrigram(rosenborg)
Team_SetNumGamesWon(rosenborg, 10).
print(Team_GetName(rosenborg))
print(Team_GetTrigram(rosenborg))
print(Team_getNumGamesWon(rosenborg))
print(Team_getNumGamesDraw(rosenborg))
print(Team_getNumberOfGoalsFor(rosenborg))
print(Team_getNumberOfGoalsAgainst(rosenborg))

# TASK 2
#datalist ser slik ut: [TriHome, ScoreHome, TriVis, ScorVis]
def Game_New(dataList):
    newGame = [dataList[0], dataList[1], dataList[2], dataList[3]]
    return newGame

def Team_GetHomeTrigram(game):
    return 

def Team_SetHomeTrigram(homeTeam, trigram):



