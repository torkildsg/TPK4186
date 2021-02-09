
# Task 1

def Team_New(name, trigram, gamesWon, gamesLost, gamesDraw, numberOfGoalsFor, numberOfGoalsAgainst):
    newTeam = [name, trigram, gamesWon, gamesLost, gamesDraw, numberOfGoalsFor, numberOfGoalsAgainst] 
    return newTeam

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
"""
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
"""

# Task 2

def Game_New(trigramHometeam, hometeamScore, trigramVisitorteam, visitorteamScore):
    newGame = {"homeTrigram": trigramHometeam, "scoreHometeam": hometeamScore, "visitorTrigram": trigramVisitorteam, "scoreVisitorteam": visitorteamScore}
    return newGame

def Team_GetHomeTrigram(game):
    return game["homeTrigram"] 

def Team_SetHomeTrigram(game, newTrigram):
    game["homeTrigram"] = newTrigram

def Team_GetVisitorTrigram(game):
    return game["visitorTrigram"]

def Team_SetVisitorTrigram(game, newTrigram):
    game["visitorTrigram"] = newTrigram


# Task 3

def Championship_New():
    championship = {"teamName":[],"teamTrigram":[],"games":[]} 
    return championship

def Championship_LookForTeam(championship, trigram):
    if(trigram in championship["teamTrigram"]):
        return trigram
    else:
        return print("The team '" + trigram + "' does not participate in this championship.")
 
def Championship_NewTeam(team, trigram, championship):
    championship["teamName"].append(team)
    championship["teamTrigram"].append(trigram)

def Championship_GetTeams(championship):
    return championship["teamName"]

def Championship_NewGame(trigramHometeam, hometeamScore, trigramVisitorteam, visitorteamScore, championship):
    game = [str(trigramHometeam), hometeamScore, str(trigramVisitorteam), visitorteamScore]
    championship["games"].append(game)

def Championship_GetGames(championship):
    return championship["games"]


# Task 4 (testing)
cup = Championship_New()
oddbk = Championship_NewTeam("oddbk", "ODD", cup)
rosenborgbk = Championship_NewTeam("rosenborgbk", "RBK", cup)



finale = Championship_NewGame("ODD", "RBK", 3, 2, cup)
semi = Championship_NewGame("VIF", "LYN", 1, 2, cup)
"""print(Championship_GetGames(cup))
print(Championship_GetTeams(cup))
print(Championship_LookForTeam(cup, "LKL"))"""



# Task 5
def Print_Team(team):
    print("Trigram: " + Team_GetTrigram(team) + "\nGames won: " + str(Team_GetNumGamesWon(team)) + "\nGames draw: " 
    + str(Team_GetNumGamesDraw(team)) + "\nGoals scored: " + str(Team_GetNumOfGoalsFor(team)) + "\nGoals conceded: " 
    + str(Team_GetNumOfGoalsAgainst(team)) + "\nPoints: " + str(Team_TotalPoints(team)))

def Print_Game(game, championship):
    if(game in championship["games"]):
        print(game)
    else:
        print("The game does not exist.")

# Testing task 5
#Print_Game(finale, cup)
#Print_Team(rosenborg)
#print(Championship_GetGames(cup))


def Print_ChampionshipDescription(championship):
    teamnames = Championship_GetTeams(championship)
    teamtrigrams = championship["teamTrigram"]
    games = Championship_GetGames(championship)

    print("#Name"+" "+"Code".rjust(25)+"\n")
    for i in range(0,len(teamnames)):
        print(teamnames[i]+" " + teamtrigrams[i].rjust(30-len(teamnames[i]))+"\n")

    print("#Home code"+"    "+"Home score"+"    "+"#Visitor code"+"    "+"Visitor score"+"\n")

    for game in games:
        print(game[0] + "           " + game[2]+ "             " + str(game[1])+ "           " + str(game[3])+"\n")

 

# Testing task 5
"""
Print_Game(finale, cup)
Print_Team(rosenborgbk)
Print_ChampionshipDescription(cup)
"""

#Task 6
import csv
tsv_file = open("PremierLeague2019-2020-Description.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")

def Import_Championship():
    championship_1 = Championship_New()
    for row in read_tsv:
        if (len(row)==2) and (row[0] != "#Name"):
            Championship_NewTeam(row[0],row[1],championship_1)
        elif (len(row)==4) and (row[0] != "#Home code"):
            Championship_NewGame(row[0],row[2],row[1],row[3],championship_1)    
    Print_ChampionshipDescription(championship_1)

#Testing task 6
Import_Championship()