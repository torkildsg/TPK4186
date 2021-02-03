
# Task 1

def Team_New(name, trigram, gamesWon, gamesLost, gamesDraw, numberOfGoalsFor, numberOfGoalsAgainst):
    return [name, trigram, gamesWon, gamesLost, gamesDraw, numberOfGoalsFor, numberOfGoalsAgainst]

def Team_GetName(team):
    return team[0]

def Team_SetName(team, name):
    team[0] = name

def Team_SetTrigram(team, trigram):
    if(len(trigram)>3):
        print("Trigram cant be more than three characters.")
    else:
        team[1] = trigram

def Team_GetTrigram(team):
    return team[1]

def Team_SetNumGamesWon(team, gamesWon):
        team[2] = gamesWon
    
def Team_GetNumGamesWon(team):
    return team[2]

def Team_SetNumGamesLost(team, gamesLost):
    team[3] = gamesLost

def Team_GetNumGamesDraw(team):
    return team[4]

def Team_SetNumGamesDraw(team, gamesDraw):
    team[4] = gamesDraw

def Team_TotalPoints(team):
    totalPoints = Team_GetNumGamesWon(team) * 3 + Team_GetNumGamesDraw(team) 
    return totalPoints

def Team_SetNumOfGoalsFor(team, numOfGoalsFor):
    team[5] = numOfGoalsFor

def Team_GetNumOfGoalsFor(team):
    return team[5]

def Team_SetNumOfGoalsAgainst(team, numOfGoalsAgainst):
    team[6] = numOfGoalsAgainst

def Team_GetNumOfGoalsAgainst(team):
    return team[6]

def Team_goalDifference(team):
    goalDifference = Team_GetNumOfGoalsFor(team) - Team_GetNumOfGoalsAgainst(team)
    return goalDifference


# Testing task 1

rosenborg = Team_New("Rosenborg", "RBK", 0 , 0, 0, 0, 0)
Team_GetName(rosenborg)
Team_GetTrigram(rosenborg)
Team_SetNumGamesWon(rosenborg, 10)
Team_SetNumGamesDraw(rosenborg, 8)
Team_SetNumOfGoalsFor(rosenborg, 20)
Team_SetNumOfGoalsAgainst(rosenborg, 5)
Team_SetTrigram(rosenborg, "RBBK")
print(Team_GetName(rosenborg))
print(Team_GetTrigram(rosenborg))
print(Team_GetNumGamesWon(rosenborg))
print(Team_GetNumGamesDraw(rosenborg))
print(Team_GetNumOfGoalsFor(rosenborg))
print(Team_GetNumOfGoalsAgainst(rosenborg))
print(Team_goalDifference(rosenborg))
print(Team_TotalPoints(rosenborg))



# Task 3

def Championship_New():
    championship = dict()
    return championship

def Championship_LookForTeam(championship, trigram):
    return championship.get(trigram)

def Championship_NewTeam(team, trigram, championship):
    newTeam = {trigram: team}
    championship.update(newTeam)

def Championship_GetTeams(championship):
    participants = []
    for trigram in championship:
        participants.append(trigram)
    return participants

def Championship_NewGame(homeTrigram, visitorTrigram, championship):
    game = [homeTrigram, visitorTrigram]
    championship.append(game)

def Championship_GetGames(championship):
    games = []
    for game in championship:
        games.append(championship.get(game))
    return games

# Task 4 (testing)



# Task 5

def Print_Team(team):
    print("Trigram: " + Team_GetTrigram(team) + "\nGames won: " + Team_GetNumGamesWon(team)
        + "\nGames draw: " + Team_GetNumGamesDraw(team) + "\nGoals scored: " + Team_GetNumOfGoalsFor(team) + "\nGoals conceded: " + Team_GetNumOfGoalsAgainst(team)
                + "\nPoints: " + Team_TotalPoints(team))

def Print_Game(game):
    print()









