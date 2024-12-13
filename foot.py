from scrapData import * 
from teamData import *
S = Scraper()

def last_X_Games_Result(listOfResult,team):
    team = team.lower()
    win,draw,loose = 0,0,0
    totalOfGame = len(listOfResult)
    for result in listOfResult:
        result = result.split()
        if (team in result[0] and int(result[1]) > int(result[3])) or (team in result[2] and int(result[3]) > int(result[1])):
            print("wiiiiin " , result)
            win+=1
        elif (int(result[1]) == int(result[3])):
            print("draw " , result)
            draw+=1
        else:
            print("loose " , result)
            loose+=1

    print(f"Win {win} {int((win/totalOfGame) * 100)}  %  Draw {win} {int((draw/totalOfGame) * 100)} %  Loose {win} {int((loose/totalOfGame) * 100)} %  Total games {totalOfGame}")
    return



data = teamData()

team1 = "Arsenal"
last_X_Games_Result(Get_Last_X_Games_Result(S,team1),team1)