from scrapData import * 
from teamData import *
from discord_webhook import DiscordWebhook
import itertools

S = Scraper()
Z = SZcraper(False)
data = teamData()

now = datetime.now()
months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
current_day_number = now.day
current_year = now.year  # Year (e.g., 2025)
current_month = now.month

def last_X_Games_Result(stats,listOfResult,url=""):
    if len(listOfResult) == 0:
        return -1
    team =  stats.name
    win,draw,loose = 0,0,0
    totalOfGame = len(listOfResult)
    
    stats.last_x_game_list = []
    stats.last_x_game_win = []
    stats.last_x_game_draw = []
    stats.last_x_game_loose = []
    stats.last_x_game_list_score = []
    stats.last_x_game_win_score = []
    stats.last_x_game_draw_score = []
    stats.last_x_game_loose_score = []
    stats.last_x_game_list_league_or_not = []
    stats.last_x_game_win_league_or_not = []
    stats.last_x_game_draw_league_or_not = []
    stats.last_x_game_loose_league_or_not = []
    stats.last_x_game_list_away_or_home = []
    stats.last_x_game_away_list = []
    stats.last_x_game_away_score = []
    stats.last_x_game_home_list = []
    stats.last_x_game_home_score = []
    stats.last_x_game_win_draw_or_loose = []
    stats.last_x_game_win_draw_or_loose_away = []
    stats.last_x_game_win_draw_or_loose_home = []

    
    for result in listOfResult:
        result = result.split()
        #print("res " , result)
        if (team in result[0] and int(result[1]) > int(result[3])) or (team in result[2] and int(result[3]) > int(result[1])):
            win+=1
            
            stats.last_x_game_win_draw_or_loose.append("W")
            if team in result[2]:
                stats.last_x_game_win_draw_or_loose_away.append("W")
                stats.last_x_game_list_away_or_home.append("A")
                stats.nb_of_win_away+=1
                stats.nb_of_game_away +=1
                stats.last_x_game_away_list.append(result[0]+"_"+result[2])
                stats.last_x_game_away_score.append(result[1]+"_"+result[3])
                stats.last_x_game_win.append(result[0]+"_"+result[2])
                stats.last_x_game_win_score.append(result[1]+"_"+result[3])
                stats.nb_of_goal_scored+=int(result[3])
                stats.nb_of_goal_scored_away+=int(result[3])
                stats.nb_of_goal_conceded+=int(result[1])
                stats.nb_of_goal_conceded_away+=int(result[1])
                stats.last_x_game_list.append(result[0]+"_"+result[2])
                stats.last_x_game_list_score.append(result[1]+"_"+result[3])

                res = pos_league_team(result[0])
                if res == -1:
                    stats.last_x_game_list_league_or_not.append("X")
                    stats.last_x_game_win_league_or_not.append("X")
                else:
                    if stats.league_of_the_team == data.all_league_name[res]:
                        stats.last_x_game_list_league_or_not.append("L")
                        stats.last_x_game_win_league_or_not.append("L")
                    else:
                        stats.last_x_game_list_league_or_not.append("N")
                        stats.last_x_game_win_league_or_not.append("N")
    
            else:
                stats.last_x_game_win_draw_or_loose_home.append("W")
                stats.last_x_game_list_away_or_home.append("H")
                stats.nb_of_win_home+=1
                stats.nb_of_game_home +=1
                stats.last_x_game_home_list.append(result[2]+"_"+result[0])
                stats.last_x_game_home_score.append(result[3]+"_"+result[1])
                stats.last_x_game_win.append(result[2]+"_"+result[0])
                stats.last_x_game_win_score.append(result[3]+"_"+result[1])
                stats.nb_of_goal_scored+=int(result[1])
                stats.nb_of_goal_scored_home+=int(result[1])
                stats.nb_of_goal_conceded+=int(result[3])
                stats.nb_of_goal_conceded_home+=int(result[3])
                stats.last_x_game_list.append(result[2]+"_"+result[0])
                stats.last_x_game_list_score.append(result[3]+"_"+result[1])
                res = pos_league_team(result[2])
                if res == -1:
                    stats.last_x_game_list_league_or_not.append("X")
                    stats.last_x_game_win_league_or_not.append("X")
                else:
                    if stats.league_of_the_team == data.all_league_name[res]:
                        stats.last_x_game_list_league_or_not.append("L")
                        stats.last_x_game_win_league_or_not.append("L")
                    else:
                        stats.last_x_game_list_league_or_not.append("N")
                        stats.last_x_game_win_league_or_not.append("N")
        elif (int(result[1]) == int(result[3])):
            stats.last_x_game_win_draw_or_loose.append("D")
            if team in result[2]:
                stats.last_x_game_win_draw_or_loose_away.append("D")
                stats.last_x_game_list_away_or_home.append("A")
                stats.nb_of_game_away +=1
                stats.nb_of_draw_away+=1
                stats.last_x_game_draw.append(result[0]+"_"+result[2])
                stats.last_x_game_draw_score.append(result[1]+"_"+result[3])
                stats.last_x_game_away_list.append(result[0]+"_"+result[2])
                stats.last_x_game_away_score.append(result[1]+"_"+result[3])
                stats.nb_of_goal_scored+=int(result[3])
                stats.nb_of_goal_scored_away+=int(result[3])
                stats.nb_of_goal_conceded+=int(result[1])
                stats.nb_of_goal_conceded_away+=int(result[1])
                stats.last_x_game_list.append(result[0]+"_"+result[2])
                stats.last_x_game_list_score.append(result[1]+"_"+result[3])
                res = pos_league_team(result[0])
                if res == -1:
                    stats.last_x_game_list_league_or_not.append("X")
                    stats.last_x_game_draw_league_or_not.append("X")
                else:
                    if stats.league_of_the_team == data.all_league_name[res]:
                        stats.last_x_game_list_league_or_not.append("L")
                        stats.last_x_game_draw_league_or_not.append("L")
                    else:
                        stats.last_x_game_list_league_or_not.append("N")
                        stats.last_x_game_draw_league_or_not.append("N")

            else:
                stats.last_x_game_win_draw_or_loose_home.append("D")
                stats.last_x_game_list_away_or_home.append("H")
                stats.nb_of_draw_home+=1
                stats.nb_of_game_home +=1
                stats.last_x_game_draw.append(result[2]+"_"+result[0])
                stats.last_x_game_draw_score.append(result[3]+"_"+result[1])
                stats.last_x_game_home_list.append(result[2]+"_"+result[0])
                stats.last_x_game_home_score.append(result[3]+"_"+result[1])
                stats.nb_of_goal_scored+=int(result[1])
                stats.nb_of_goal_scored_home+=int(result[1])
                stats.nb_of_goal_conceded+=int(result[3])
                stats.nb_of_goal_conceded_home+=int(result[3])
                stats.last_x_game_list.append(result[2]+"_"+result[0])
                stats.last_x_game_list_score.append(result[3]+"_"+result[1])
                res = pos_league_team(result[2])
                if res == -1:
                    stats.last_x_game_list_league_or_not.append("X")
                    stats.last_x_game_draw_league_or_not.append("X")
                else:
                    if stats.league_of_the_team == data.all_league_name[res]:
                        stats.last_x_game_list_league_or_not.append("L")
                        stats.last_x_game_draw_league_or_not.append("L")
                    else:
                        stats.last_x_game_list_league_or_not.append("N")
                        stats.last_x_game_draw_league_or_not.append("N")
            

            draw+=1
        else:
            stats.last_x_game_win_draw_or_loose.append("L")
            if team in result[2]:
                stats.last_x_game_win_draw_or_loose_away.append("L")
                stats.last_x_game_list_away_or_home.append("A")
                stats.nb_of_game_away +=1
                stats.nb_of_loose_away+=1
                stats.last_x_game_loose.append(result[0]+"_"+result[2])
                stats.last_x_game_loose_score.append(result[1]+"_"+result[3])
                stats.last_x_game_away_list.append(result[0]+"_"+result[2])
                stats.last_x_game_away_score.append(result[1]+"_"+result[3])
                stats.nb_of_goal_scored+=int(result[3])
                stats.nb_of_goal_scored_away+=int(result[3])
                stats.nb_of_goal_conceded+=int(result[1])
                stats.nb_of_goal_conceded_away+=int(result[1])
                stats.last_x_game_list.append(result[0]+"_"+result[2])
                stats.last_x_game_list_score.append(result[1]+"_"+result[3])
                res = pos_league_team(result[0])
                if res == -1:
                    stats.last_x_game_list_league_or_not.append("X")
                    stats.last_x_game_loose_league_or_not.append("X")
                else:    
                    if stats.league_of_the_team == data.all_league_name[res]:
                        stats.last_x_game_list_league_or_not.append("L")
                        stats.last_x_game_loose_league_or_not.append("L")
                    else:
                        stats.last_x_game_list_league_or_not.append("N")
                        stats.last_x_game_loose_league_or_not.append("N")

            else:
                stats.last_x_game_win_draw_or_loose_home.append("L")
                stats.last_x_game_list_away_or_home.append("H")
                stats.nb_of_loose_home+=1
                stats.nb_of_game_home +=1
                stats.last_x_game_loose.append(result[2]+"_"+result[0])
                stats.last_x_game_loose_score.append(result[3]+"_"+result[1])
                stats.last_x_game_home_list.append(result[2]+"_"+result[0])
                stats.last_x_game_home_score.append(result[3]+"_"+result[1])
                stats.nb_of_goal_scored+=int(result[1])
                stats.nb_of_goal_conceded+=int(result[3])
                stats.nb_of_goal_conceded_home+=int(result[3])
                stats.nb_of_goal_scored_home+=int(result[1])
                stats.last_x_game_list.append(result[2]+"_"+result[0])
                stats.last_x_game_list_score.append(result[3]+"_"+result[1])
                res = pos_league_team(result[2])
                if res == -1:
                    stats.last_x_game_list_league_or_not.append("X")
                    stats.last_x_game_loose_league_or_not.append("X")
                else:
                    if stats.league_of_the_team == data.all_league_name[res]:
                        stats.last_x_game_list_league_or_not.append("L")
                        stats.last_x_game_loose_league_or_not.append("L")
                    else:
                        stats.last_x_game_list_league_or_not.append("N")
                        stats.last_x_game_loose_league_or_not.append("N")
            
            loose+=1
    
    stats.team_url = url
    stats.nb_of_game = len(listOfResult)
    stats.nb_of_win = win
    stats.nb_of_draw = draw
    stats.nb_of_loose = loose
    stats.win_rate_percent = int((win/totalOfGame) * 100)
    stats.draw_rate_percent = int((draw/totalOfGame) * 100)
    stats.loose_rate_percent = int((loose/totalOfGame) * 100)
    stats.nb_of_goal_scored_per_match = round(float(stats.nb_of_goal_scored/stats.nb_of_game),1)
    stats.nb_of_goal_conceded_per_match = round(float(stats.nb_of_goal_conceded/stats.nb_of_game),1)
    
    if stats.nb_of_game_away > 0:
        stats.win_rate_percent_away = int((stats.nb_of_win_away/stats.nb_of_game_away) * 100)
        stats.loose_rate_percent_away = int((stats.nb_of_loose_away/stats.nb_of_game_away) * 100)
        stats.draw_rate_percent_away = int((stats.nb_of_draw_away/stats.nb_of_game_away) * 100)
        stats.nb_of_goal_conceded_per_match_away = round(float(stats.nb_of_goal_conceded_away/stats.nb_of_game_away),1)
        stats.nb_of_goal_scored_per_match_away = round(float(stats.nb_of_goal_scored_away/stats.nb_of_game_away),1)
        
    if stats.nb_of_game_home > 0:
        stats.win_rate_percent_home = int((stats.nb_of_win_home/stats.nb_of_game_home) * 100)
        stats.loose_rate_percent_home = int((stats.nb_of_loose_home/stats.nb_of_game_home) * 100)
        stats.draw_rate_percent_home = int((stats.nb_of_draw_home/stats.nb_of_game_home) * 100)
        stats.nb_of_goal_scored_per_match_home = round(float(stats.nb_of_goal_scored_home/stats.nb_of_game_home),1)
        stats.nb_of_goal_conceded_per_match_home = round(float(stats.nb_of_goal_conceded_home/stats.nb_of_game_home),1)
    return

def convert_nb_to_100(nb,len_all_nb):
    return int((nb*100)/len_all_nb) + 30

def get_team_league(team):
    try:
        data.pos_league_team = pos_league_team(team)
        league_of_the_team = data.all_league_name[data.pos_league_team]
        return league_of_the_team
    except:
        return ("ok")
def get_score_based_on_the_league(team):
    try:
        pos_on_the_league = Position_Of_A_Team_On_Its_League(S,team)
        data.pos_league_team = pos_league_team(team)
        league_of_the_team = data.all_league_name[data.pos_league_team]
        score_based_on_league_and_league_place = int(data.default_score_based_on_the_league[data.pos_league_team] * convert_nb_to_100(data.nb_of_team_on_all_league[data.pos_league_team] - pos_on_the_league - 1, data.nb_of_team_on_all_league[data.pos_league_team]))
        if pos_league_team(team) == -1:
            return 100
        if score_based_on_league_and_league_place < 100:
            return 100
        return score_based_on_league_and_league_place + 10000
    except:
        #import traceback
        #traceback.print_exc()
            
        return 100

def little_ratio_based_on_team_place_on_league(team,team2,teamScore,score_based_on_league_and_league_place,type=2):
    try:
        pos_on_the_league = Position_Of_A_Team_On_Its_League(S,team)
        pos_on_the_league2 = Position_Of_A_Team_On_Its_League(S,team2)
        data.pos_league_team = pos_league_team(team)
        d2 = pos_league_team(team2)
        z = ((teamScore-score_based_on_league_and_league_place)/teamScore)
        if score_based_on_league_and_league_place >= teamScore:
            z = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place)
        try:
            if score_based_on_league_and_league_place < teamScore:
                z = abs(z)
                if type == 1:
                    z = 1 - abs(z)
                    z = abs(z)
                return z
            
            else:
                z = abs(z)
                if type == 1:
                    z = 1 - abs(z)
                    z = abs(z)
                return z
        except:
            return 0    
    except:
        return 0

def get_the_score_of_a_team(team,nbOfGameToAnalyze=20):    
    score = 0
    statsT = TeamStat()
    statsT.name = team

    if statsT.name not in data.allTeam:
        #print("team not in the data default score is 1")
        return 1
        #return score_based_on_league_and_league_place + 100
    

    score_based_on_league_and_league_place = get_score_based_on_the_league(statsT.name)
    allTeamTxt = print_file_info("allteam.txt").lower().split("\n")
    team_pos = allTeamTxt.index(statsT.name.lower())
    try:
        x = last_X_Games_Result(statsT,Get_Last_X_Games_Result(S,statsT.name,team_pos,nbOfGameToAnalyze))
        if x == -1:
            #print("Team didnt play a game this year or a bug happend so the score is 1")
            return 1
    except:
        return score_based_on_league_and_league_place
    
    index = 0
    diffScore = 0
    finalScore = 0
    teamGoal = 0
    oppenentGoal = 0

    for teams in statsT.last_x_game_list:
        isLastFive = False
        x2Points = 1
        if index in [0,1,2,3,4]:
            isLastFive = True
            x2Points = 2.5
        #print("ok " , teams , index , 20)
        #print("caca " , statsT.last_x_game_list_league_or_not[index] , statsT.last_x_game_list_league_or_not)
        facedTeam = teams.split("_")[0]
        teamScore = get_score_based_on_the_league(facedTeam)
        #print("timtim " , teamScore , facedTeam , score_based_on_league_and_league_place)
        teamGoal = int(statsT.last_x_game_list_score[index].split("_")[1])
        oppenentGoal = int(statsT.last_x_game_list_score[index].split("_")[0])
        #print("ME " , teamGoal , " OPS " , oppenentGoal)
        if teamScore < score_based_on_league_and_league_place:
            if statsT.last_x_game_list_away_or_home[index] == "A":
                if statsT.last_x_game_win_draw_or_loose[index] == "W":
                    #print("kci  1")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (1.1 - little_ratio_based_on_team_place_on_league(facedTeam,statsT.name,teamScore,score_based_on_league_and_league_place,1))
                    # 1 - diffscore
                    diffScore = 1 - abs(diffScore)
                    resultGoal = teamGoal * 5 - oppenentGoal * 25
                    finalScore+= abs(diffScore + abs(resultGoal))
                if statsT.last_x_game_win_draw_or_loose[index] == "D":
                    #print("kci  2")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.1 - little_ratio_based_on_team_place_on_league(facedTeam,statsT.name,teamScore,score_based_on_league_and_league_place,1))
                    diffScore = 1 - abs(diffScore)
                    resultGoal = teamGoal * 5 - oppenentGoal * 25
                    finalScore-= abs(diffScore + abs(resultGoal))
                    if finalScore >= 0:
                        finalScore = finalScore * -1
        
                if statsT.last_x_game_win_draw_or_loose[index] == "L":
                    #print("kci  3")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.5 + little_ratio_based_on_team_place_on_league(facedTeam,statsT.name,teamScore,score_based_on_league_and_league_place,2))
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 5 - oppenentGoal * 25
                    finalScore-= abs(diffScore + abs(resultGoal))
                    if finalScore >= 0:
                        finalScore = finalScore * -1
        
                
            elif statsT.last_x_game_list_away_or_home[index] == "H":
                if statsT.last_x_game_win_draw_or_loose[index] == "W":
                    #print("kci  4")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (1 - little_ratio_based_on_team_place_on_league(facedTeam,statsT.name,teamScore,score_based_on_league_and_league_place,1))
                    diffScore = 1 - abs(diffScore)
                    resultGoal = teamGoal * 10 - oppenentGoal * 20
                    finalScore+= abs(diffScore + abs(resultGoal))
                
                if statsT.last_x_game_win_draw_or_loose[index] == "D":
                    #print("kci  5")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.2 + little_ratio_based_on_team_place_on_league(facedTeam,statsT.name,teamScore,score_based_on_league_and_league_place,1))
                    diffScore = 1 - abs(diffScore)
                    resultGoal = teamGoal * 10 - oppenentGoal * 20
                    finalScore-= abs(diffScore + abs(resultGoal))
                    if finalScore >= 0:
                        finalScore = finalScore * -1
        
                
                if statsT.last_x_game_win_draw_or_loose[index] == "L":
                    #print("kci  6")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.6 + little_ratio_based_on_team_place_on_league(facedTeam,statsT.name,teamScore,score_based_on_league_and_league_place,2))
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 10 - oppenentGoal * 20
                    finalScore-= abs(diffScore + abs(resultGoal))
                    if finalScore >= 0:
                        finalScore = finalScore * -1
        
                
        else:
            if statsT.last_x_game_list_away_or_home[index] == "A":
                if statsT.last_x_game_win_draw_or_loose[index] == "W":
                    #print("kci  7")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.6 - little_ratio_based_on_team_place_on_league(facedTeam,statsT.name,teamScore,score_based_on_league_and_league_place,2))
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 25 - oppenentGoal * 5
                    finalScore+= abs(diffScore + abs(resultGoal))
                
                if statsT.last_x_game_win_draw_or_loose[index] == "D":
                    #print("kci  8")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.2 - little_ratio_based_on_team_place_on_league(facedTeam,statsT.name,teamScore,score_based_on_league_and_league_place,2))
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 25 - oppenentGoal * 5
                    finalScore+= (diffScore + abs(resultGoal))
                
                if statsT.last_x_game_win_draw_or_loose[index] == "L":
                    #print("kci  9")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (0.75 - little_ratio_based_on_team_place_on_league(facedTeam,statsT.name,teamScore,score_based_on_league_and_league_place,1))
                    diffScore = 1 - abs(diffScore)
                    resultGoal = teamGoal * 25 - oppenentGoal * 5
                    finalScore-= abs(diffScore + abs(resultGoal))
                    if finalScore >= 0:
                        finalScore = finalScore * -1
        
                
            elif statsT.last_x_game_list_away_or_home[index] == "H":
                if statsT.last_x_game_win_draw_or_loose[index] == "W":
                    #print("kci  10")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.5 - little_ratio_based_on_team_place_on_league(facedTeam,statsT.name,teamScore,score_based_on_league_and_league_place,2))
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 20 - oppenentGoal * 10
                    finalScore+= abs(diffScore + abs(resultGoal))
                
                if statsT.last_x_game_win_draw_or_loose[index] == "D":
                    #print("kci  11")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.1 - little_ratio_based_on_team_place_on_league(facedTeam,statsT.name,teamScore,score_based_on_league_and_league_place,2))
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 20 - oppenentGoal * 10
                    finalScore+= (diffScore + abs(resultGoal))
                
                if statsT.last_x_game_win_draw_or_loose[index] == "L":
                    #print("kci  12")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (0.8 - little_ratio_based_on_team_place_on_league(facedTeam,statsT.name,teamScore,score_based_on_league_and_league_place,1))
                    diffScore = 1 - abs(diffScore)
                    resultGoal = teamGoal * 20 - oppenentGoal * 10
                    finalScore-= abs(diffScore + abs(resultGoal))
                    if finalScore >= 0:
                        finalScore = finalScore * -1
        
                
        
        #print("DIIF SCORE " , diffScore , " Final Score "  , finalScore , f" {team} VS {facedTeam} result: {statsT.last_x_game_win_draw_or_loose[index]} is oppenent weaker ? {teamScore < score_based_on_league_and_league_place}")
        #print(" Final Score "  , finalScore , f" {team} VS {facedTeam} result: {statsT.last_x_game_win_draw_or_loose[index]} is oppenent weaker ? {teamScore < score_based_on_league_and_league_place}")
        
        #print("zebi " , statsT.last_x_game_list_away_or_home, " zebo")
        index+=1
    finalScore = int(finalScore)
    #print("Score basique " , score_based_on_league_and_league_place)
    if finalScore < 0:
        return score_based_on_league_and_league_place - abs(finalScore) , statsT.win_rate_percent
    else:
        return score_based_on_league_and_league_place + finalScore , statsT.win_rate_percent

    
def get_the_score_of_the_main_team(team,nbOfGameToAnalyze=20,NoPrint=True):
    # if NoPrint == True:
    #     print("Program could take long time to run depending on how many games to analyze you put :)")
    # if NoPrint == False:
    #     print("Wait beetween 1 to 3 minutes until it get the data of your team")
    x_team_score = 0
    index = 0
    statsTeam = TeamStat()
    statsTeam.name = team
    statsTeam.name = statsTeam.name.lower()

    if statsTeam.name not in data.allTeam:
        #print("cacacaca " , statsTeam.name)
        #print("team not in the data default score is 1")
        return 1
    statsTeam.pos_on_the_league = Position_Of_A_Team_On_Its_League(S,statsTeam.name)
    data.pos_league_team = pos_league_team(statsTeam.name)
    statsTeam.league_of_the_team = data.all_league_name[data.pos_league_team]
    allTeamTxt = print_file_info("allteam.txt").lower().split("\n")
    team_pos = allTeamTxt.index(statsTeam.name.lower())
    urlOfTeam = get_url_of_a_team(team_pos)
    last_X_Games_Result(statsTeam,Get_Last_X_Games_Result(S,statsTeam.name,team_pos,nbOfGameToAnalyze),urlOfTeam)
    diffScore = 0
    finalScore = 0
    teamGoal = 0
    oppenentGoal = 0
    score_based_on_league_and_league_place = get_score_based_on_the_league(statsTeam.name)
    score = score_based_on_league_and_league_place
    #send_message_discord(f"Country {data.country_of_the_team[data.pos_league_team]}")
    if NoPrint == True:
        print(f"Country {data.country_of_the_team[data.pos_league_team]}")
        print(f"Default score of {team}:  {score} (based on it position on the league and the league the team play in)")
        print(f"Position of team on the {data.all_league_name[data.pos_league_team]}: {statsTeam.pos_on_the_league}")
        print(f"Last {len(statsTeam.last_x_game_list)} games of the team:")
        print(statsTeam.last_x_game_list)
        print("The score: ")
        print(statsTeam.last_x_game_list_score)
        print("The outcome: ")
        print(statsTeam.last_x_game_win_draw_or_loose)
    for teams in statsTeam.last_x_game_list:
        isLastFive = False
        x2Points = 1
        if index in [0,1,2,3,4]:
            #print("Last 5 games")
            isLastFive = True
            x2Points = 2.5
        facedTeam = teams.split("_")[0]
        if facedTeam not in data.allTeam:
            #print(f"skiipping {facedTeam} team not in the list of team")
            index+=1
            continue
        #print("faceeeeee " , facedTeam)
        win_rate_nb = 0
        try:
            x_team_score , win_rate_nb = get_the_score_of_a_team(facedTeam)
        except:
            x_team_score = get_score_based_on_the_league(facedTeam)
        #print("Scooore of my team " , score_based_on_league_and_league_place , " Oppenent score " , x_team_score)
        #print("----Next----")
        teamScore = x_team_score
        teamGoal = int(statsTeam.last_x_game_list_score[index].split("_")[1])
        oppenentGoal = int(statsTeam.last_x_game_list_score[index].split("_")[0])
        #print("ME " , teamGoal , " OPS " , oppenentGoal)

        if teamScore < score_based_on_league_and_league_place:
            if statsTeam.last_x_game_list_away_or_home[index] == "A":
                if statsTeam.last_x_game_win_draw_or_loose[index] == "W":
                    #print("ici  1")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (1.1 - little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,1))
                    # 1 - diffscore
                    diffScore = 1 - abs(diffScore)
                    resultGoal = teamGoal * 5 - oppenentGoal * 25
                    finalScore+= abs(diffScore + abs(resultGoal))
                    #print('ok")
                if statsTeam.last_x_game_win_draw_or_loose[index] == "D":
                    #print("ici  2")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.1 - little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,1))
                    diffScore = 1 - abs(diffScore)
                    resultGoal = teamGoal * 5 - oppenentGoal * 25
                    finalScore-= abs(diffScore + abs(resultGoal))
                    if finalScore >= 0:
                        finalScore = finalScore * -1
        
                    #print(finalScore,little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,1),(score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place)
                    #print('ok")
                if statsTeam.last_x_game_win_draw_or_loose[index] == "L":
                    #print("ici  3")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.5 + little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,2))
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 5 - oppenentGoal * 25
                    finalScore-= abs(diffScore + abs(resultGoal))
                    if finalScore >= 0:
                        finalScore = finalScore * -1
        
                
            elif statsTeam.last_x_game_list_away_or_home[index] == "H":
                if statsTeam.last_x_game_win_draw_or_loose[index] == "W":
                    #print("ici  4")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (1 - little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,1))
                    diffScore = 1 - abs(diffScore)
                    resultGoal = teamGoal * 10 - oppenentGoal * 20
                    finalScore+= abs(diffScore + abs(resultGoal))
                    #print('ok")
                if statsTeam.last_x_game_win_draw_or_loose[index] == "D":
                    #print("ici  5")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.2 + little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,1))
                    diffScore = 1 - abs(diffScore)
                    resultGoal = teamGoal * 10 - oppenentGoal * 20
                    finalScore-= abs(diffScore + abs(resultGoal))
                    if finalScore >= 0:
                        finalScore = finalScore * -1
        
                    #print('ok")
                    #print(finalScore,little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,1),(score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place)
                if statsTeam.last_x_game_win_draw_or_loose[index] == "L":
                    #print("ici  6")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.6 + little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,2))
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 10 - oppenentGoal * 20
                    finalScore-= abs(diffScore + abs(resultGoal))
                    if finalScore >= 0:
                        finalScore = finalScore * -1
        
                
        else:
            if statsTeam.last_x_game_list_away_or_home[index] == "A":
                if statsTeam.last_x_game_win_draw_or_loose[index] == "W":
                    #print("ici  7")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.6 - little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,2))
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 25 - oppenentGoal * 5
                    finalScore+= abs(diffScore + abs(resultGoal))
                    #print('ok")
                if statsTeam.last_x_game_win_draw_or_loose[index] == "D":
                    #print("ici  8")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.2 - little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,2))
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 25 - oppenentGoal * 5
                    finalScore+= (diffScore + abs(resultGoal))
                    #print(finalScore,little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,2),(score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place)
                    #print('ok")
                if statsTeam.last_x_game_win_draw_or_loose[index] == "L":
                    #print("ici  9")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (0.75 - little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,1))
                    diffScore = 1 - abs(diffScore)
                    resultGoal = teamGoal * 25 - oppenentGoal * 5
                    finalScore-= abs(diffScore + abs(resultGoal))
                    if finalScore >= 0:
                        finalScore = finalScore * -1
        
                
            elif statsTeam.last_x_game_list_away_or_home[index] == "H":
                if statsTeam.last_x_game_win_draw_or_loose[index] == "W":
                    #print("ici  10")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.5 - little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,2))
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 20 - oppenentGoal * 10
                    finalScore+= abs(diffScore + abs(resultGoal))
                    #print('ok")
                if statsTeam.last_x_game_win_draw_or_loose[index] == "D":
                    #print("ici  11")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (2.1 - little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,2))
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 20 - oppenentGoal * 10
                    finalScore+= (diffScore + abs(resultGoal))
                    #print(finalScore,little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,2),(score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place)
                    #print('ok")
                if statsTeam.last_x_game_win_draw_or_loose[index] == "L":
                    #print("ici  12")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * x2Points * (0.8 - little_ratio_based_on_team_place_on_league(facedTeam,statsTeam.name,teamScore,score_based_on_league_and_league_place,1))
                    diffScore = 1 - abs(diffScore)
                    resultGoal = teamGoal * 20 - oppenentGoal * 10
                    finalScore-= abs(diffScore + abs(resultGoal))
                    if finalScore >= 0:
                        finalScore = finalScore * -1
        
        finalScore = int(finalScore)    
        #print("Score basique " , score_based_on_league_and_league_place)

        if finalScore < 0:
            score-=abs(finalScore)
        else:
            score+=finalScore
        if NoPrint == True:
            print(f"Score de base du {team}: {score_based_on_league_and_league_place} , Score actuel du {team}: {score} et de {facedTeam}: {x_team_score}" , f" result: {statsTeam.last_x_game_win_draw_or_loose[index]} is oppenent weaker ? {teamScore < score_based_on_league_and_league_place}")
        index+=1
    if NoPrint == True:
        print(f"Score final de  {team} : {score}")
    return score
    


def is_num(nb):
    try:
        int(nb)
        return True
    except:
        return False


def check_data_entered_is_good(country_nb,leen):
    if is_num(country_nb) == False:
        print("Wrong data entered exiting the program")
        quit()
    
    if is_num(country_nb) == True and (int(country_nb) < 1 or int(country_nb) > leen):
        print("Wrong data entered exiting the program")
        exit()


def choose_a_team(nbnb):
    for i in range(len(data.country_of_the_team)):
        print(f"{i+1}. {data.country_of_the_team[i]}")
    print()
    print()
    country_nb = input(f"Country of Team {nbnb} (choose between 1 and {len(data.country_of_the_team)}): ")
    check_data_entered_is_good(country_nb , len(data.country_of_the_team))

    inputError = 0
    specialInput = False
    for i in range(len(data.allTeam_[int(country_nb) - 1])):
        if len(data.allTeam_[int(country_nb) - 1][0].strip()) > 1:
            print(f"{i + 1}. {data.allTeam_[int(country_nb) - 1][i].strip()}")    
            specialInput = True
        elif len(data.allTeam_[int(country_nb) - 1][i].strip()) > 1:
            print(f"{i}. {data.allTeam_[int(country_nb) - 1][i].strip()}")
        else:
            inputError+=1

    team_nb = input(f"Choose your team (choose between 1 and {len(data.allTeam_[int(country_nb) - 1]) - inputError}): ")
    team_nb = int(team_nb)
    if specialInput == True:
        team_nb-=1
    check_data_entered_is_good(team_nb , len(data.allTeam_[int(country_nb) - 1]) - inputError)
    
    return data.allTeam_[int(country_nb) - 1][int(team_nb)].strip()

def calc_pourcent_of_win(nb1,nb2):
    try:
        return (round(nb1/(nb2/100),1))
    except:
        return 1


def print_result_info(team1,score_of_team1,team2,score_of_team2,idxx):
    alphaElem = str(idxx)
    print(f"Score of {team1}: {score_of_team1} , Score of {team2}: {score_of_team2}")
    score_of_team1 = abs(score_of_team1)
    score_of_team2 = abs(score_of_team2)
    
    p1 = str(calc_pourcent_of_win(score_of_team1,score_of_team1+score_of_team2))
    p2 = str(calc_pourcent_of_win(score_of_team2,score_of_team1+score_of_team2))
    league_team_1 = get_team_league(team1)
    write_into_file("league.txt",alphaElem + " " + league_team_1 + "\n")
    if score_of_team1 > score_of_team2:
        if score_of_team2 * 1.25 < score_of_team1:
            print(f"{team2} will loose against {team1}")
            #send_message_discord(f"{team2} will loose against {team1}")
            #send_message_discord(f"{team2} {p2} will loose against {team1} {p1}")
            odds = get_odds(S,team1,team2,"W")

            if len(odds) > 2 and "." not in odds or odds == "-999":
                odds = get_odds(Z,team1,team2,"W",True)
            
            if len(odds) > 2 and "." not in odds:
                odds = "-999"            
            
            send_message_discord(f"{team1} {p1} WIN VS {team2} {p2} ODDS {odds}")
            write_into_file("match.txt", alphaElem + " " + team1 + " " + team2 + "\n")
            write_into_file("result.txt",alphaElem + " " + team1 + "\n")
            write_into_file("odds.txt",alphaElem + " " + odds + "\n")
            write_into_file("percent.txt",alphaElem + " " + p1+ "-" + p2 + "\n")

        else:
            print(f"{team1} have a win ratio a little bit higher than {team2} but the most likely outcome is a draw")
            #send_message_discord(f"{team1} have a win ratio a little bit higher than {team2} but the most likely outcome is a draw")
            odds = get_odds(S,team1,team2,"D")
            if len(odds) > 2 and "." not in odds or odds == "-999":
                odds = get_odds(Z,team1,team2,"D",True)
            
            if len(odds) > 2 and "." not in odds:
                odds = "-999"
            
            odds = str(odds)

            send_message_discord(f"{team1} {p1} DRAW VS {team2} {p2} ODDS {odds}")
            write_into_file("match.txt", alphaElem + " " + team1 + " " + team2 + "\n")
            write_into_file("result.txt",alphaElem + " " + team1 + " DRAW" + "\n")
            write_into_file("odds.txt",alphaElem + " " + odds + "\n")
            write_into_file("percent.txt",alphaElem + " " + p1+ "-" + p2 + "\n")


        print(f"{team1} have a win rate of {calc_pourcent_of_win(score_of_team1,score_of_team1+score_of_team2)} against {team2}")
        print(f"{team2} have a win rate of {calc_pourcent_of_win(score_of_team2,score_of_team1+score_of_team2)} against {team1}")
        # send_message_discord(f"{team1} have a win rate of {calc_pourcent_of_win(score_of_team1,score_of_team1+score_of_team2)} against {team2}")
        # send_message_discord(f"{team2} have a win rate of {calc_pourcent_of_win(score_of_team2,score_of_team1+score_of_team2)} against {team1}")
    else:
        if score_of_team1 * 1.25 < score_of_team2:
            print(f"{team1} will loose against {team2}")
            #send_message_discord(f"{team1} will loose against {team2}")
            odds = get_odds(Z,team1,team2,"L")
            if len(odds) > 2 and "." not in odds or odds == "-999":
                odds = get_odds(S,team1,team2,"L",True)
            
            if len(odds) > 2 and "." not in odds:
                odds = "-999"
            
            
            send_message_discord(f"{team2} {p2} WIN VS {team1} {p1} ODDS {odds}")
            write_into_file("match.txt", alphaElem + " " + team1 + " " + team2 + "\n")
            write_into_file("result.txt",alphaElem + " " + team2 + "\n")
            write_into_file("odds.txt",alphaElem + " " + odds + "\n")
            write_into_file("percent.txt",alphaElem + " " + p2+ "-" + p1 + "\n")
        else:
            print(f"{team2} have a win ratio a little bit higher than {team1} but the most likely outcome is a draw")
            #send_message_discord(f"{team2} have a win ratio a little bit higher than {team1} but the most likely outcome is a draw")
            odds = get_odds(S,team1,team2,"D")
            if len(odds) > 2 and "." not in odds or odds == "-999":
                odds = get_odds(Z,team1,team2,"D",True)
            if len(odds) > 2 and "." not in odds:
                odds = "-999"
            
            send_message_discord(f"{team2} {p2} DRAW VS {team1} {p1} ODDS {odds}")
            write_into_file("match.txt", alphaElem + " " + team1 + " " + team2 + "\n")
            write_into_file("result.txt",alphaElem + " " + team2 + " DRAW" + "\n")
            write_into_file("odds.txt",alphaElem + " " + odds + "\n")
            write_into_file("percent.txt",alphaElem + " " + p2+ "-" + p1 + "\n")
        
        print(f"{team2} have a win rate of {calc_pourcent_of_win(score_of_team2,score_of_team1+score_of_team2)} against {team1}")
        print(f"{team1} have a win rate of {calc_pourcent_of_win(score_of_team1,score_of_team1+score_of_team2)} against {team2}")
        #send_message_discord(f"{team2} have a win rate of {calc_pourcent_of_win(score_of_team2,score_of_team1+score_of_team2)} against {team1}")
        #send_message_discord(f"{team1} have a win rate of {calc_pourcent_of_win(score_of_team1,score_of_team1+score_of_team2)} against {team2}")

def send_message_discord(msg):
    discordUrl = print_file_info("discordWebhookUrl.txt")
    try:
        urls = discordUrl
        webhook = DiscordWebhook(url=urls, content=msg)
        response = webhook.execute()
    except:
       pass

def team_vs_team(team1,team2,idxx):
    try:
        team1 = team1.replace(" ","-")
        team2 = team2.replace(" ","-")

        #nbOfGameToAnalyze = input("How many games to you want the bot to analyze? (Min 1 Max 20)" + "\n" + "The bigger the number is the better the analyze will be:")
        #check_data_entered_is_good(nbOfGameToAnalyze,20)
        nbOfGameToAnalyze = 20
        #send_message_discord(f"{team1} vs {team2}")
        print(f"{team1} vs {team2}")

        # score_of_team1 = abs(get_the_score_of_the_main_team(team1,int(nbOfGameToAnalyze),False))
        # #print("+"*200)
        # score_of_team2 = abs(get_the_score_of_the_main_team(team2,int(nbOfGameToAnalyze),False))

        x = get_the_score_of_the_main_team(team1,int(nbOfGameToAnalyze),False)
        print("+"*200)
        y = get_the_score_of_the_main_team(team2,int(nbOfGameToAnalyze),False)
        score_of_team1 = abs(x)
        if x > 0 and y < 0 :
            score_of_team1 += abs(y) * 2
        print("+"*200)
        score_of_team2 = abs(y)
        if x < 0 and y > 0:
            score_of_team2 += abs(x) * 2
        
        if calc_pourcent_of_win(score_of_team2,score_of_team1+score_of_team2) > 80 or calc_pourcent_of_win(score_of_team1,score_of_team1+score_of_team2) > 80:
            time.sleep(300)
            score_of_team1 = (get_the_score_of_the_main_team(team1,int(nbOfGameToAnalyze),False))
            #print("+"*200)
            score_of_team2 = abs(get_the_score_of_the_main_team(team2,int(nbOfGameToAnalyze),False))
            print_result_info(team1,score_of_team1,team2,score_of_team2,idxx)
        else:
            print_result_info(team1,score_of_team1,team2,score_of_team2,idxx)
    except:
        pass


def generate_alphabet_list():
    result = []
    for length in range(1, 4):  # For 1-letter, 2-letter, and 3-letter combinations
        result.extend(
            ''.join(letters) for letters in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=length)
        )
    return result


from os import sys

time.sleep(50 * int(sys.argv[1]))
reset_file("result.txt")
reset_file("percent.txt")
reset_file("match.txt")
reset_file("odds.txt")
reset_file("league.txt")

reset_file("ckk.txt")
matches = get_match_of_the_day(S)

if len(matches) < 4:
    print("not enough matches")
    quit()

def balanced_sublists(lst, n):
    # Calculate the size of each sublist
    avg = len(lst) / n
    sublists = []
    last = 0.0

    for i in range(n):
        # Determine the indices for slicing
        start = int(last)
        last += avg
        end = int(last)
        sublists.append(lst[start:end])

    return sublists

# Distribute the original list into 5 balanced sublists
sublists = balanced_sublists(matches, 5)

while len(sublists) < 5:
    sublists.append(['a', 'b'])  # Add a "fake" list with placeholder elements

# Unpack into variables
list1, list2, list3, list4, list5 = sublists


try:
    list1, list2, list3, list4, list5 = sublists
    list_of_list = [list1,list2,list3,list4,list5]
    current_list = list_of_list[int(sys.argv[1]) - 1]
except:
    print("You must put arguments beetween 1 and 5")
    quit()

print(current_list)
print("Match of the day to analyze " , current_list)
idx = (int(sys.argv[1])) * 10

allTeamTxt = print_file_info("allteam.txt").lower().split("\n")

if idx == 1:
    send_message_discord("New Day New Match but Cristiano Ronaldo is still the goat")

for match in current_list:
    m = match.split("#####")
    print(m[0],m[1])
    time.sleep(10)
    team_pos1 , team_pos2 = allTeamTxt.index(m[0].lower()),allTeamTxt.index(m[1].lower())
    played1 , played2 = has_Team_Played_since_september(S,m[0],team_pos1),has_Team_Played_since_september(S,m[1],team_pos2)
    if len(m[0]) > 0 and len(m[1]) > 0 and played1 == True and played2 == True:
        team_vs_team(m[0],m[1],idx)
        time.sleep(60)
    idx+=1