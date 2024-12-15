from scrapData import * 
from teamData import *
S = Scraper()
data = teamData()

def last_X_Games_Result(stats,listOfResult):
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
                stats.nb_of_goal_scored+=int(result[1])
                stats.nb_of_goal_scored_away+=int(result[1])
                stats.nb_of_goal_conceded+=int(result[3])
                stats.nb_of_goal_conceded_away+=int(result[3])
                stats.last_x_game_list.append(result[0]+"_"+result[2])
                stats.last_x_game_list_score.append(result[1]+"_"+result[3])

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
    
            else:
                stats.last_x_game_win_draw_or_loose_home.append("W")
                stats.last_x_game_list_away_or_home.append("H")
                stats.nb_of_win_home+=1
                stats.nb_of_game_home +=1
                stats.last_x_game_home_list.append(result[2]+"_"+result[0])
                stats.last_x_game_home_score.append(result[3]+"_"+result[1])
                stats.last_x_game_win.append(result[2]+"_"+result[0])
                stats.last_x_game_win_score.append(result[3]+"_"+result[1])
                stats.nb_of_goal_scored+=int(result[3])
                stats.nb_of_goal_scored_home+=int(result[3])
                stats.nb_of_goal_conceded+=int(result[1])
                stats.nb_of_goal_conceded_home+=int(result[1])
                stats.last_x_game_list.append(result[2]+"_"+result[0])
                stats.last_x_game_list_score.append(result[3]+"_"+result[1])
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
                stats.nb_of_goal_scored+=int(result[1])
                stats.nb_of_goal_scored_away+=int(result[1])
                stats.nb_of_goal_conceded+=int(result[3])
                stats.nb_of_goal_conceded_away+=int(result[3])
                stats.last_x_game_list.append(result[0]+"_"+result[2])
                stats.last_x_game_list_score.append(result[1]+"_"+result[3])
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

            else:
                stats.last_x_game_win_draw_or_loose_home.append("D")
                stats.last_x_game_list_away_or_home.append("H")
                stats.nb_of_draw_home+=1
                stats.nb_of_game_home +=1
                stats.last_x_game_draw.append(result[2]+"_"+result[0])
                stats.last_x_game_draw_score.append(result[3]+"_"+result[1])
                stats.last_x_game_home_list.append(result[2]+"_"+result[0])
                stats.last_x_game_home_score.append(result[3]+"_"+result[1])
                stats.nb_of_goal_scored+=int(result[3])
                stats.nb_of_goal_scored_home+=int(result[3])
                stats.nb_of_goal_conceded+=int(result[1])
                stats.nb_of_goal_conceded_home+=int(result[1])
                stats.last_x_game_list.append(result[2]+"_"+result[0])
                stats.last_x_game_list_score.append(result[3]+"_"+result[1])
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
                stats.nb_of_goal_scored+=int(result[1])
                stats.nb_of_goal_scored_away+=int(result[1])
                stats.nb_of_goal_conceded+=int(result[3])
                stats.nb_of_goal_conceded_away+=int(result[3])
                stats.last_x_game_list.append(result[0]+"_"+result[2])
                stats.last_x_game_list_score.append(result[1]+"_"+result[3])
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

            else:
                stats.last_x_game_win_draw_or_loose_home.append("L")
                stats.last_x_game_list_away_or_home.append("H")
                stats.nb_of_loose_home+=1
                stats.nb_of_game_home +=1
                stats.last_x_game_loose.append(result[2]+"_"+result[0])
                stats.last_x_game_loose_score.append(result[3]+"_"+result[1])
                stats.last_x_game_home_list.append(result[2]+"_"+result[0])
                stats.last_x_game_home_score.append(result[3]+"_"+result[1])
                stats.nb_of_goal_scored+=int(result[3])
                stats.nb_of_goal_conceded+=int(result[1])
                stats.nb_of_goal_conceded_home+=int(result[1])
                stats.nb_of_goal_scored_home+=int(result[3])
                stats.last_x_game_list.append(result[2]+"_"+result[0])
                stats.last_x_game_list_score.append(result[3]+"_"+result[1])
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
            
            loose+=1
    
    stats.nb_of_game = len(listOfResult)
    stats.nb_of_win = win
    stats.nb_of_draw = draw
    stats.nb_of_loose = loose
    stats.win_rate_percent = int((win/totalOfGame) * 100)
    stats.draw_rate_percent = int((draw/totalOfGame) * 100)
    stats.loose_rate_percent = int((loose/totalOfGame) * 100)
    stats.nb_of_goal_scored_per_match = round(float(stats.nb_of_goal_scored/stats.nb_of_game),1)
    stats.nb_of_goal_conceded_per_match = round(float(stats.nb_of_goal_conceded/stats.nb_of_game),1)
    
    stats.win_rate_percent_away = int((stats.nb_of_win_away/stats.nb_of_game_away) * 100)
    stats.loose_rate_percent_away = int((stats.nb_of_loose_away/stats.nb_of_game_away) * 100)
    stats.draw_rate_percent_away = int((stats.nb_of_draw_away/stats.nb_of_game_away) * 100)
    
    stats.win_rate_percent_home = int((stats.nb_of_win_home/stats.nb_of_game_home) * 100)
    stats.loose_rate_percent_home = int((stats.nb_of_loose_home/stats.nb_of_game_home) * 100)
    stats.draw_rate_percent_home = int((stats.nb_of_draw_home/stats.nb_of_game_home) * 100)
    
    stats.nb_of_goal_conceded_per_match_away = round(float(stats.nb_of_goal_conceded_away/stats.nb_of_game_away),1)
    stats.nb_of_goal_scored_per_match_away = round(float(stats.nb_of_goal_scored_away/stats.nb_of_game_away),1)
    stats.nb_of_goal_scored_per_match_home = round(float(stats.nb_of_goal_scored_home/stats.nb_of_game_home),1)
    stats.nb_of_goal_conceded_per_match_home = round(float(stats.nb_of_goal_conceded_home/stats.nb_of_game_home),1)
    
    return

def print_all_data(stats):
    print(f"Team Name: {stats.name}")
    print(f"Points: {stats.point}")
    print(f"Position in the League: {stats.pos_on_the_league}")
    print(f"League of the Team: {stats.league_of_the_team}")
    print(f"Last {len(stats.last_x_game_list)} Games: {stats.last_x_game_list}")
    print(f"Last X Game Win Draw or Loose: {stats.last_x_game_win_draw_or_loose}")
    print(f"Last X Game League or Not: {stats.last_x_game_list_league_or_not}")
    print(f"Wins in Last {len(stats.last_x_game_list)} Games: {stats.last_x_game_win}")
    print(f"Last X Game Win League or Not: {stats.last_x_game_win_league_or_not}")
    print(f"Draws in Last {len(stats.last_x_game_list)} Games: {stats.last_x_game_draw}")
    print(f"Last X Game Draw League or Not: {stats.last_x_game_draw_league_or_not}")
    print(f"Losses in Last {len(stats.last_x_game_list)} Games: {stats.last_x_game_loose}")
    print(f"Last X Game Loose League or Not: {stats.last_x_game_loose_league_or_not}")
    print(f"Scores of Last {len(stats.last_x_game_list)} Games: {stats.last_x_game_list_score}")
    print(f"Scores in Wins: {stats.last_x_game_win_score}")
    print(f"Scores in Draws: {stats.last_x_game_draw_score}")
    print(f"Scores in Losses: {stats.last_x_game_loose_score}")
    print(f"Number of Wins: {stats.nb_of_win}")
    print(f"Number of Losses: {stats.nb_of_loose}")
    print(f"Number of Draws: {stats.nb_of_draw}")
    print(f"Total Number of Games Played: {stats.nb_of_game}")
    print(f"Win Rate: {stats.win_rate_percent}%")
    print(f"Loss Rate: {stats.loose_rate_percent}%")
    print(f"Draw Rate: {stats.draw_rate_percent}%")
    print(f"Goals Scored: {stats.nb_of_goal_scored}")
    print(f"Goals Conceded: {stats.nb_of_goal_conceded}")
    print(f"Goals Scored per Match: {stats.nb_of_goal_scored_per_match}")
    print(f"Goals Conceded per Match: {stats.nb_of_goal_conceded_per_match}")
    print(f"Last X Game Away List: {stats.last_x_game_away_list}")
    print(f"Last X Game Win Draw or Loose Away: {stats.last_x_game_win_draw_or_loose_away}")
    print(f"Last X Game Away Score: {stats.last_x_game_away_score}")
    print(f"Number of Wins Away: {stats.nb_of_win_away}")
    print(f"Number of Losses Away: {stats.nb_of_loose_away}")
    print(f"Number of Draws Away: {stats.nb_of_draw_away}")
    print(f"Total Number of Away Games Played: {stats.nb_of_game_away}")
    print(f"Win Rate Away: {stats.win_rate_percent_away}%")
    print(f"Loss Rate Away: {stats.loose_rate_percent_away}%")
    print(f"Draw Rate Away: {stats.draw_rate_percent_away}%")
    print(f"Goals Scored Away: {stats.nb_of_goal_scored_away}")
    print(f"Goals Conceded Away: {stats.nb_of_goal_conceded_away}")
    print(f"Goals Scored per Match Away: {stats.nb_of_goal_scored_per_match_away}")
    print(f"Goals Conceded per Match Away: {stats.nb_of_goal_conceded_per_match_away}")
    print(f"Last X Game Home List: {stats.last_x_game_home_list}")
    print(f"Last X Game Win Draw or Loose Home: {stats.last_x_game_win_draw_or_loose_home}")
    print(f"Last X Game Home List: {stats.last_x_game_home_score}")
    print(f"Number of Wins Home: {stats.nb_of_win_home}")
    print(f"Number of Losses Home: {stats.nb_of_loose_home}")
    print(f"Number of Draws Home: {stats.nb_of_draw_home}")
    print(f"Total Number of Home Games Played: {stats.nb_of_game_home}")
    print(f"Win Rate Home: {stats.win_rate_percent_home}%")
    print(f"Loss Rate Home: {stats.loose_rate_percent_home}%")
    print(f"Draw Rate Home: {stats.draw_rate_percent_home}%")
    print(f"Goals Scored Home: {stats.nb_of_goal_scored_home}")
    print(f"Goals Conceded Home: {stats.nb_of_goal_conceded_home}")
    print(f"Goals Scored per Match Home: {stats.nb_of_goal_scored_per_match_home}")
    print(f"Goals Conceded per Match Home: {stats.nb_of_goal_conceded_per_match_home}")
    

def convert_nb_to_100(nb,len_all_nb):
    return int((nb*100)/len_all_nb)

def get_score_based_on_the_league(team):
    try:
        pos_on_the_league = Position_Of_A_Team_On_Its_League(S,team)
        data.pos_league_team = pos_league_team(team)
        league_of_the_team = data.all_league_name[data.pos_league_team]
        score_based_on_league_and_league_place = int(data.default_score_based_on_the_league[data.pos_league_team] * convert_nb_to_100(data.nb_of_team_on_all_league[data.pos_league_team] - pos_on_the_league - 1, data.nb_of_team_on_all_league[data.pos_league_team]))
        
        if pos_league_team(team) == -1:
            return 100
        return score_based_on_league_and_league_place
    except:
        return 10

def get_the_score_of_a_team(team):
    
    # Regarder toute les stats sauf les adversaires des adversaires affronter bref
    score = 0
    statsT = TeamStat()
    statsT.name = team

    if statsT.name not in data.allTeam:
        #print("team not in the team data default score is 1")
        return 100

    score_based_on_league_and_league_place = get_score_based_on_the_league(statsT.name)
    # # print("Team Name " , stats.name)
    # print("League name " , data.all_league_name[data.pos_league_team])
    # print("Position on the league " , stats.pos_on_the_league)
    # print("Country " , data.country_of_the_team[data.pos_league_team])
    allTeamTxt = print_file_info("allteam.txt").split("\n")
    team_pos = allTeamTxt.index(statsT.name)
    last_X_Games_Result(statsT,Get_Last_X_Games_Result(S,statsT.name,team_pos))
    # print(statsT.name)
    # print("Scooore " , score_based_on_league_and_league_place)
    # print(statsT.last_x_game_win_draw_or_loose)
    # print(statsT.last_x_game_list)
    # print(statsT.last_x_game_list_away_or_home)
    
    index = 0
    diffScore = 0
    finalScore = 0
    teamGoal = 0
    oppenentGoal = 0

    for teams in statsT.last_x_game_list:
        print("ok " , teams , index , 20)
        facedTeam = teams.split("_")[0]
        teamScore = get_score_based_on_the_league(facedTeam)
        #print("timtim " , teamScore , facedTeam , score_based_on_league_and_league_place)
        teamGoal = int(statsT.last_x_game_list_score[index].split("_")[1])
        oppenentGoal = int(statsT.last_x_game_list_score[index].split("_")[0])
        #print("ME " , teamGoal , " OPS " , oppenentGoal)
        if teamScore < score_based_on_league_and_league_place:
            if statsT.last_x_game_list_away_or_home[index] == "A":
                if statsT.last_x_game_win_draw_or_loose[index] == "W":
                    ##print("ici  1")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * 1.1
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 5 - oppenentGoal * 25
                    finalScore+= (diffScore + resultGoal)
                if statsT.last_x_game_win_draw_or_loose[index] == "D":
                    ##print("ici  2")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * 2.1
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 5 - oppenentGoal * 25
                    finalScore+= (diffScore + resultGoal)
                
                if statsT.last_x_game_win_draw_or_loose[index] == "L":
                    ##print("ici  3")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * 2.5
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 5 - oppenentGoal * 25
                    finalScore+= (diffScore + resultGoal)
                
            elif statsT.last_x_game_list_away_or_home[index] == "H":
                if statsT.last_x_game_win_draw_or_loose[index] == "W":
                    ##print("ici  4")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 10 - oppenentGoal * 20
                    finalScore+= (diffScore + resultGoal)
                
                if statsT.last_x_game_win_draw_or_loose[index] == "D":
                    ##print("ici  5")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * 2.2
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 10 - oppenentGoal * 20
                    finalScore+= (diffScore + resultGoal)
                
                if statsT.last_x_game_win_draw_or_loose[index] == "L":
                    ##print("ici  6")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * 2.6
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 10 - oppenentGoal * 20
                    finalScore+= (diffScore + resultGoal)
                
        else:
            if statsT.last_x_game_list_away_or_home[index] == "A":
                if statsT.last_x_game_win_draw_or_loose[index] == "W":
                    ##print("ici  7")
                    diffScore = (teamScore/score_based_on_league_and_league_place) * 100 * 2.6
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 25 - oppenentGoal * 5
                    finalScore+= (diffScore + resultGoal)
                
                if statsT.last_x_game_win_draw_or_loose[index] == "D":
                    ##print("ici  8")
                    diffScore = (teamScore/score_based_on_league_and_league_place) * 100 * 2.2
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 25 - oppenentGoal * 5
                    finalScore+= (diffScore + resultGoal)
                
                if statsT.last_x_game_win_draw_or_loose[index] == "L":
                    ##print("ici  9")
                    diffScore = (teamScore/score_based_on_league_and_league_place) * 100 * 0.75
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 25 - oppenentGoal * 5
                    finalScore+= (diffScore + resultGoal)
                
            elif statsT.last_x_game_list_away_or_home[index] == "H":
                if statsT.last_x_game_win_draw_or_loose[index] == "W":
                    ##print("ici  10")
                    diffScore = (teamScore/score_based_on_league_and_league_place) * 100 * 2.5
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 20 - oppenentGoal * 10
                    finalScore+= (diffScore + resultGoal)
                
                if statsT.last_x_game_win_draw_or_loose[index] == "D":
                    ##print("ici  11")
                    diffScore = (teamScore/score_based_on_league_and_league_place) * 100 * 2.1
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 20 - oppenentGoal * 10
                    finalScore+= (diffScore + resultGoal)
                
                if statsT.last_x_game_win_draw_or_loose[index] == "L":
                    ##print("ici  12")
                    diffScore = (teamScore/score_based_on_league_and_league_place) * 100 * 0.8
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 20 - oppenentGoal * 10
                    finalScore+= (diffScore + resultGoal)
                
        
        #print("DIIF SCORE " , diffScore , " Final Score "  , finalScore , f" {team} VS {facedTeam} result: {statsT.last_x_game_win_draw_or_loose[index]} is oppenent weaker ? {teamScore < score_based_on_league_and_league_place}")
        #print("zebi " , statsT.last_x_game_list_away_or_home, " zebo")
        index+=1

    finalScore = int(finalScore)
    #print("Score basique " , score_based_on_league_and_league_place)
    if finalScore < 0:
        return score_based_on_league_and_league_place - abs(finalScore)
    else:
        return score_based_on_league_and_league_place + finalScore

    
def get_the_score_of_the_main_team(team):
    x_team_score = 0
    index = 0
    statsTeam = TeamStat()
    #stats.name = "man-city"
    statsTeam.name = team

    statsTeam.name = statsTeam.name.lower()

    if statsTeam.name not in data.allTeam:
        print("team not in the team data default score is 1")
        return 1

    statsTeam.pos_on_the_league = Position_Of_A_Team_On_Its_League(S,statsTeam.name)
    data.pos_league_team = pos_league_team(statsTeam.name)
    statsTeam.league_of_the_team = data.all_league_name[data.pos_league_team]
    # print("Team Name " , stats.name)
    # print("League name " , data.all_league_name[data.pos_league_team])
    # print("Position on the league " , stats.pos_on_the_league)
    # print("Country " , data.country_of_the_team[data.pos_league_team])
    allTeamTxt = print_file_info("allteam.txt").split("\n")
    team_pos = allTeamTxt.index(statsTeam.name)
    last_X_Games_Result(statsTeam,Get_Last_X_Games_Result(S,statsTeam.name,team_pos))
    #print(vars(stats))
    diffScore = 0
    finalScore = 0
    teamGoal = 0
    oppenentGoal = 0
    score_based_on_league_and_league_place = get_score_based_on_the_league(statsTeam.name)
    score = score_based_on_league_and_league_place
    print("default score of " , team ,  " " , score)
    for teams in statsTeam.last_x_game_list:
        facedTeam = teams.split("_")[0]
        print("faceeeeee " , facedTeam)
        x_team_score = get_the_score_of_a_team(facedTeam)
        print("Scooore of my team " , score_based_on_league_and_league_place , " Oppenent score " , x_team_score)
        teamScore = x_team_score
        teamGoal = int(statsTeam.last_x_game_list_score[index].split("_")[1])
        oppenentGoal = int(statsTeam.last_x_game_list_score[index].split("_")[0])
        #print("ME " , teamGoal , " OPS " , oppenentGoal)
        if teamScore < score_based_on_league_and_league_place:
            if statsTeam.last_x_game_list_away_or_home[index] == "A":
                if statsTeam.last_x_game_win_draw_or_loose[index] == "W":
                    #print("ici  1")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * 1.1
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 5 - oppenentGoal * 25
                    finalScore+= (diffScore + resultGoal)
                if statsTeam.last_x_game_win_draw_or_loose[index] == "D":
                    #print("ici  2")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * 2.1
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 5 - oppenentGoal * 25
                    finalScore+= (diffScore + resultGoal)
                
                if statsTeam.last_x_game_win_draw_or_loose[index] == "L":
                    #print("ici  3")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * 2.5
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 5 - oppenentGoal * 25
                    finalScore+= (diffScore + resultGoal)
                
            elif statsTeam.last_x_game_list_away_or_home[index] == "H":
                if statsTeam.last_x_game_win_draw_or_loose[index] == "W":
                    #print("ici  4")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 10 - oppenentGoal * 20
                    finalScore+= (diffScore + resultGoal)
                
                if statsTeam.last_x_game_win_draw_or_loose[index] == "D":
                    #print("ici  5")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * 2.2
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 10 - oppenentGoal * 20
                    finalScore+= (diffScore + resultGoal)
                
                if statsTeam.last_x_game_win_draw_or_loose[index] == "L":
                    #print("ici  6")
                    diffScore = ((score_based_on_league_and_league_place-teamScore)/score_based_on_league_and_league_place) * 100 * 2.6
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 10 - oppenentGoal * 20
                    finalScore+= (diffScore + resultGoal)
                
        else:
            if statsTeam.last_x_game_list_away_or_home[index] == "A":
                if statsTeam.last_x_game_win_draw_or_loose[index] == "W":
                    #print("ici  7")
                    diffScore = (teamScore/score_based_on_league_and_league_place) * 100 * 2.6
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 25 - oppenentGoal * 5
                    finalScore+= (diffScore + resultGoal)
                
                if statsTeam.last_x_game_win_draw_or_loose[index] == "D":
                    #print("ici  8")
                    diffScore = (teamScore/score_based_on_league_and_league_place) * 100 * 2.2
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 25 - oppenentGoal * 5
                    finalScore+= (diffScore + resultGoal)
                
                if statsTeam.last_x_game_win_draw_or_loose[index] == "L":
                    #print("ici  9")
                    diffScore = (teamScore/score_based_on_league_and_league_place) * 100 * 0.75
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 25 - oppenentGoal * 5
                    finalScore+= (diffScore + resultGoal)
                
            elif statsTeam.last_x_game_list_away_or_home[index] == "H":
                if statsTeam.last_x_game_win_draw_or_loose[index] == "W":
                    #print("ici  10")
                    diffScore = (teamScore/score_based_on_league_and_league_place) * 100 * 2.5
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 20 - oppenentGoal * 10
                    finalScore+= (diffScore + resultGoal)
                
                if statsTeam.last_x_game_win_draw_or_loose[index] == "D":
                    #print("ici  11")
                    diffScore = (teamScore/score_based_on_league_and_league_place) * 100 * 2.1
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 20 - oppenentGoal * 10
                    finalScore+= (diffScore + resultGoal)
                
                if statsTeam.last_x_game_win_draw_or_loose[index] == "L":
                    #print("ici  12")
                    diffScore = (teamScore/score_based_on_league_and_league_place) * 100 * 0.8
                    diffScore = abs(diffScore)
                    resultGoal = teamGoal * 20 - oppenentGoal * 10
                    finalScore+= (diffScore + resultGoal)
                
        

        finalScore = int(finalScore)
        
        #print("Score basique " , score_based_on_league_and_league_place)
        if finalScore < 0:
            score-=abs(finalScore)
        else:
            score+=finalScore
        print("Diiif scoree " , diffScore , f" Score finito finit {score}" , f" {team} VS {facedTeam} result: {statsTeam.last_x_game_win_draw_or_loose[index]} is oppenent weaker ? {teamScore < score_based_on_league_and_league_place}")
        #print("zebi " , statsTeam.last_x_game_list_away_or_home, " zebo")
        index+=1
        
    
    #print(statsTeam.last_x_game_list)
    #print(statsTeam.last_x_game_home_score)
    #print(statsTeam.last_x_game_win_draw_or_loose)
    print(f"Score final de  {team} : {score}")
    return score
    #print_all_data(statsTeam)



a = get_the_score_of_the_main_team("liverpool")
print(a)

# data = teamData()
# stats = TeamStat()
# #stats.name = "man-city"
# stats.name = "liverpool"

# stats.name = stats.name.lower()

# if stats.name not in data.allTeam:
#     print("team not in the team data")
#     exit()

# stats.pos_on_the_league = Position_Of_A_Team_On_Its_League(S,stats.name)
# data.pos_league_team = pos_league_team(stats.name)
# stats.league_of_the_team = data.all_league_name[data.pos_league_team]
# # print("Team Name " , stats.name)
# # print("League name " , data.all_league_name[data.pos_league_team])
# # print("Position on the league " , stats.pos_on_the_league)
# # print("Country " , data.country_of_the_team[data.pos_league_team])
# allTeamTxt = print_file_info("allteam.txt").split("\n")
# team_pos = allTeamTxt.index(stats.name)
# last_X_Games_Result(stats,Get_Last_X_Games_Result(S,stats.name,team_pos))
# #print(vars(stats))

# print_all_data(stats)