
# Task 1

def Team_New(name, trigram):
    newTeam = [name, trigram, 0, 0, 0, 0, 0, 0, 0] # 2 = number of games won, 3 = number of games lost, 4 = number of games draw, 
                                                # 5 = total points, 6 = number of goals for, 7 = number of goals against, 8 = goaldifference
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

def Team_updateTotalPoints(team):
    totalPoints = Team_GetNumGamesWon(team) * 3 + Team_GetNumGamesDraw(team) 
    team[5] = totalPoints

def Team_SetNumOfGoalsFor(team, numOfGoalsFor):
    team[6] = numOfGoalsFor

def Team_GetNumOfGoalsFor(team):
    return team[6]

def Team_SetNumOfGoalsAgainst(team, numOfGoalsAgainst):
    team[7] = numOfGoalsAgainst

def Team_GetNumOfGoalsAgainst(team):
    return team[7]

def Team_updateGoalDifference(team):
    goalDifference = Team_GetNumOfGoalsFor(team) - Team_GetNumOfGoalsAgainst(team)
    team[8] = goalDifference

def Team_GetGoalDifference(team):
    Team_updateGoalDifference(team)
    return team[8]


# Testing task 1
rosenborg = Team_New("Rosenborg", "RBK")
Team_GetName(rosenborg) 
Team_GetTrigram(rosenborg)
Team_SetNumGamesWon(rosenborg, 10)
Team_SetNumGamesDraw(rosenborg, 8)
Team_SetNumOfGoalsFor(rosenborg, 20)
Team_SetNumOfGoalsAgainst(rosenborg, 5)
Team_SetTrigram(rosenborg, "RBK")
Team_updateGoalDifference(rosenborg)
Team_updateTotalPoints(rosenborg)
"""print(Team_GetName(rosenborg))
print(Team_GetTrigram(rosenborg))
print(Team_GetNumGamesWon(rosenborg))
print(Team_GetNumGamesDraw(rosenborg))
print(Team_GetNumOfGoalsFor(rosenborg))
print(Team_GetNumOfGoalsAgainst(rosenborg))
print(rosenborg)"""



# Task 2

def Game_New(trigramHometeam, hometeamScore, trigramVisitorteam, visitorteamScore):
    newGame = [trigramHometeam, hometeamScore, trigramVisitorteam, visitorteamScore]
    return newGame

def Game_GetHomeTrigram(game):
    return game[0] 

def Game_SetHomeTrigram(game, newTrigram):
    game[0] = newTrigram

def Game_GetVisitorTrigram(game):
    return game[2]

def Game_SetVisitorTrigram(game, newTrigram):
    game[2] = newTrigram

def Game_SetScoreHometeam(game, hometeamScore):
    game[1] = hometeamScore

def Game_GetScoreHometeam(game):
    return game[1]

def Game_SetScoreVisitorteam(game, visitorteamScore):
    game[3] = visitorteamScore

def Game_GetScoreVisitorteam(game):
    return game[3]


# Task 3

def Championship_New():
    championship = [dict(), []] # Alle teams kommer i dict på indeks 0, med trigram som key. Games puttes i liste på indeks 1.
    return championship

def Championship_LookForTeam(championship, trigram):
    if(trigram in championship[0]):
        return trigram
    else:
        return print("The team '" + trigram + "' does not participate in this championship.")
 
def Championship_NewTeam(team, trigram, championship):
    Championship_GetTeams(championship)[trigram] = team

def Championship_GetTeams(championship):
    return championship[0] # Må castes til en liste med .items()

def Championship_NewGame(trigramHometeam, hometeamScore, trigramVisitorteam, visitorteamScore, championship):
    game = [trigramHometeam, hometeamScore, trigramVisitorteam, visitorteamScore]
    championship[1].append(game)

def Championship_GetGames(championship):
    return championship[1]


# Task 4 (testing)
cup = Championship_New()
oddbk = Championship_NewTeam("oddbk", "ODD", cup)
rosenborgbk = Championship_NewTeam("rosenborgbk", "RBK", cup)
lyn = Championship_NewTeam("lynfk", "LYN", cup)
finale = Championship_NewGame("ODD", 3, "RBK", 2, cup)
semi = Championship_NewGame("VIF",  1, "LYN", 2, cup)


"""print(Championship_GetGames(cup))
print(Championship_GetTeams(cup))
print(Championship_LookForTeam(cup, "RBK"))"""


# Task 5
def Print_Team(team):
    print("Trigram: " + Team_GetTrigram(team) + "\nGames won: " + str(Team_GetNumGamesWon(team)) + "\nGames draw: " 
    + str(Team_GetNumGamesDraw(team)) + "\nGoals scored: " + str(Team_GetNumOfGoalsFor(team)) + "\nGoals conceded: " 
    + str(Team_GetNumOfGoalsAgainst(team)) + "\nPoints: " + str(Team_TotalPoints(team)))

"""def Print_Game(game):
    print("")"""

def Print_ChampionshipDescription(championship):
    teamnames = list(Championship_GetTeams(championship).values())
    teamtrigrams = list(Championship_GetTeams(championship).keys())
    games = Championship_GetGames(championship)

    
    print("#Name"+" "+"Code".rjust(25)+"\n")
    for i in range(0,len(teamnames)):
        print(teamnames[i]+" " + teamtrigrams[i].rjust(30-len(teamnames[i]))+"\n")

    print("#Home code"+"    "+"Home score"+"    "+"#Visitor code"+"    "+"Visitor score"+"\n")

    for game in games:
        print(str(game[0]) + "           " + str(game[1])+ "             " + str(game[2])+ "           " + str(game[3])+"\n")

# Testing task 5
#Print_Game(finale, cup)
#Print_Team(rosenborg)
#print(Championship_GetGames(cup))

"""Print_ChampionshipDescription(cup)"""


#Task 6
import csv
tsv_file = open("PremierLeague2019-2020-Description.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t") #legg til try/except

def Import_Championship():
    championship_1 = Championship_New()
    for row in read_tsv:
        if (len(row)==2) and (row[0] != "#Name"):
            Championship_NewTeam(row[0],row[1],championship_1)
        elif (len(row)==4) and (row[0] != "#Home code"):
            Championship_NewGame(row[0],row[2],row[1],row[3],championship_1)    
    #Print_ChampionshipDescription(championship_1)
    return championship_1

#Testing task 6
"""Import_Championship()"""

#Task 7:

def Championship_UpdateStatistics(championship):
    games = Championship_GetGames(championship)
    teamtrigrams = list(Championship_GetTeams(championship).keys())
    for game in games:
        tri_home = Game_GetHomeTrigram(game)
        tri_away = Game_GetVisitorTrigram(game)
        goals_home = Game_GetScoreHometeam(game)
        goals_away = Game_GetScoreVisitorteam(game)
        winner =""
        looser =""
        draw = False
        if (goals_home > goals_away):
            winner = tri_home
        elif(goals_away<goals_away):
            winner = tri_away
        elif(goals_away ==goals_home):
            draw = True
        
        

                    
    
    
    
