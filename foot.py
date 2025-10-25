from posixpath import split
from scrapData import * 
from teamData import *

S = Scraper()
data = teamData()

def last_X_Games_Result(stats,listOfResult,url="",national=False):
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
    stats.starting_xi = []
    
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
    
    if national:
        try:
            stats.starting_xi = print_file_info("starting_xi_national_team.txt").lower().split("\n")[print_file_info("nationalTeam.txt").lower().split("\n").index(stats.name)]
        except:
            stats.starting_xi = [None]
    else:
        try:
            stats.starting_xi = print_file_info("starting_xi_league_team.txt").lower().split("\n")[print_file_info("allteam.txt").lower().split("\n").index(stats.name)]
        except:
            stats.starting_xi = [None]
        
    stats.score = get_score_based_on_the_league(stats.name,national)
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

def print_all_data(stats,national=False):
    print(f"Team Name: {stats.name}")
    print(f"Team url: {stats.team_url}")
    print(f"Team default score {stats.score}")
    if national == False:
        print(f"Position in the League: {stats.pos_on_the_league}")
        print(f"League of the Team: {stats.league_of_the_team}")
    else:
        print("Current country ranking: " , stats.pos_on_the_league + 1 , "/210")
    print(f"Starting XI: {stats.starting_xi}")
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
    return int((nb*100)/len_all_nb) + 30

def get_score_based_on_the_league(team,national=False):
    national_team = print_file_info("nationalTeam.txt").lower()
    if team.lower() in national_team:
        national = True
    try:
        if national == False:
            pos_on_the_league = Position_Of_A_Team_On_Its_League(S,team,national)
            data.pos_league_team = pos_league_team(team)
            league_of_the_team = data.all_league_name[data.pos_league_team]
            score_based_on_league_and_league_place = int(data.default_score_based_on_the_league[data.pos_league_team] * convert_nb_to_100(data.nb_of_team_on_all_league[data.pos_league_team] - pos_on_the_league - 1, data.nb_of_team_on_all_league[data.pos_league_team]))
            if pos_on_the_league == -999:
                score_based_on_league_and_league_place = int(data.default_score_based_on_the_league[data.pos_league_team] * convert_nb_to_100(data.nb_of_team_on_all_league[data.pos_league_team] - int(data.nb_of_team_on_all_league[data.pos_league_team]/2) - 1, data.nb_of_team_on_all_league[data.pos_league_team]))
            if pos_league_team(team) == -1:
                return 100
            if score_based_on_league_and_league_place < 100:
                return 100
            return score_based_on_league_and_league_place + 10000
        else:
            # score_based_on_league_and_league_place = 
            # int(data.default_score_based_on_the_league[data.pos_league_team] * 
            #     convert_nb_to_100(data.nb_of_team_on_all_league[data.pos_league_team] - pos_on_the_league - 1, 
            #                       data.nb_of_team_on_all_league[data.pos_league_team]))

            national_team_list = print_file_info("nationalTeam.txt").lower().split("\n")
            pos_of_team_on_the_list = national_team_list.index(team) + 1
            score_based_on_ranking = 10 * 210 + pos_of_team_on_the_list
            score_based_on_league_and_league_place = int(score_based_on_ranking * convert_nb_to_100(210 - pos_of_team_on_the_list - 1,210))
            # print(score_based_on_ranking)
            # print(convert_nb_to_100(210 - pos_of_team_on_the_list - 1,210))
            # print(score_based_on_league_and_league_place)
            if score_based_on_league_and_league_place < 100:
                return 100
            return score_based_on_league_and_league_place + 10000

    except:   
        return 100

def little_ratio_based_on_team_place_on_league(team,team2,teamScore,score_based_on_league_and_league_place,type=2):
    try:
        # pos_on_the_league = Position_Of_A_Team_On_Its_League(S,team)
        # pos_on_the_league2 = Position_Of_A_Team_On_Its_League(S,team2)
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

def get_the_score_of_a_team(team,nbOfGameToAnalyze=20,national=False):    
    score = 0
    statsT = TeamStat()
    statsT.name = team
    national_team_list = print_file_info("nationalTeam.txt").lower().split("\n")
    national_team_list_url = print_file_info("nationalTeamUrl.txt").lower().split("\n")
    
    if national == False:
        if statsT.name not in data.allTeam:
            #print("ici 1")
            print("team not in the data default score is 1")
            return 1
            #return score_based_on_league_and_league_place + 100
    else:
        if statsT.name.lower() not in national_team_list:
            #print("ici 2")
            print("team not in the data default score is 1")
            return 1
            

    score_based_on_league_and_league_place = get_score_based_on_the_league(statsT.name,national)
    allTeamTxt = print_file_info("allteam.txt").lower().split("\n")
    if national == False:
        team_pos = allTeamTxt.index(statsT.name.lower())
    else:
        team_pos = 0
    try:
        x = last_X_Games_Result(statsT,Get_Last_X_Games_Result(S,statsT.name,team_pos,nbOfGameToAnalyze,True),national)
        
        if x == -1:
            print("Team didnt play a game this year or a bug happend so the score is 1")
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
        teamScore = get_score_based_on_the_league(facedTeam,national)
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

    
def get_the_score_of_the_main_team(team,nbOfGameToAnalyze=20,NoPrint=True,National=False,coutry_rank=0):
    if NoPrint == True:
        print("Program could take long time to run depending on how many games to analyze you put :)")
    if NoPrint == False:
        print("Wait beetween 1 to 3 minutes until it get the data of your team")
    x_team_score = 0
    index = 0
    statsTeam = TeamStat()
    statsTeam.name = team
    statsTeam.name = statsTeam.name.lower()
    #NoPrint = True
    national_team_list = print_file_info("nationalTeamAlphabeticOrder.txt").lower().split("\n")
    national_team_list_url = print_file_info("nationalTeamUrl.txt").lower().split("\n")
    
    if National == False:
        if statsTeam.name not in data.allTeam:
            #print("ici 3")
            print("team not in the data default score is 1")
            return 1
        
        statsTeam.pos_on_the_league = Position_Of_A_Team_On_Its_League(S,statsTeam.name,National)
        if statsTeam.pos_on_the_league == -999:
            return - 1
    else:
        statsTeam.pos_on_the_league = coutry_rank
        if statsTeam.name.lower() not in national_team_list:
            #print("ici 4")
            print("team not in the data default score is 1")
            return 1
    if National == False:
        data.pos_league_team = pos_league_team(statsTeam.name)
        statsTeam.league_of_the_team = data.all_league_name[data.pos_league_team]
        allTeamTxt = print_file_info("allteam.txt").lower().split("\n")
        team_pos = allTeamTxt.index(statsTeam.name.lower())
        urlOfTeam = get_url_of_a_team(team_pos)
        last_X_Games_Result(statsTeam,Get_Last_X_Games_Result(S,statsTeam.name,team_pos,nbOfGameToAnalyze),urlOfTeam)
    else:
        urlOfTeam = national_team_list_url[national_team_list.index(statsTeam.name)]
        last_X_Games_Result(statsTeam,Get_Last_X_Games_Result(S,statsTeam.name,0,nbOfGameToAnalyze,True),urlOfTeam,True)
    if NoPrint and nbOfGameToAnalyze == 999:
        print_all_data(statsTeam)
        return
        
    diffScore = 0
    finalScore = 0
    teamGoal = 0
    oppenentGoal = 0
    score_based_on_league_and_league_place = get_score_based_on_the_league(statsTeam.name,National)
    #score_based_on_league_and_league_place = 150000
    score = score_based_on_league_and_league_place
    if NoPrint == True:
        if National == False:
            print(f"Country {data.country_of_the_team[data.pos_league_team]}")
            print(f"Default score of {team}:  {score} (based on it position on the league and the league the team play in)")
            print(f"Power of the {data.all_league_name[data.pos_league_team]} :{data.default_score_based_on_the_league[data.pos_league_team]}")
            print(f"Position of team on the {data.all_league_name[data.pos_league_team]}: {statsTeam.pos_on_the_league}")
        else:
            print(team)
            print("Current country ranking: " , coutry_rank + 1 , "/ 210")
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
        if National == False:
            if facedTeam not in data.allTeam:
                print(f"skiipping {facedTeam} team not in the list of team")
                index+=1
                continue
        else:
            if facedTeam.lower() not in national_team_list:
                print(f"skiipping {facedTeam} team not in the list of team")
                index+=1
                continue
        
        #print("faceeeeee " , facedTeam)
        win_rate_nb = 0
        try:
            x_team_score , win_rate_nb = get_the_score_of_a_team(facedTeam,nbOfGameToAnalyze,National)
        except:
            
            x_team_score = get_score_based_on_the_league(facedTeam,National)
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


def same_name_team_check(league_team_based_on_position,country_nb):
    country_nb = int(country_nb)
    new_list = []
    if country_nb == 14:
        for team in league_team_based_on_position:
            if team.lower() == "rapid":
                print("ok")
                new_list.append("Rapid_AUSTRIA")
            else:
                new_list.append(team)
        return new_list
    elif country_nb == 33:
        for team in league_team_based_on_position:
            if team.lower() == "ahli":
                print("ok")
                new_list.append("Ahli_QATAR")
            else:
                new_list.append(team)
        return new_list
    elif country_nb == 21:
        for team in league_team_based_on_position:
            if team.lower() == "racing":
                print("ok")
                new_list.append("Racing_ARGENTINA")
            else:
                new_list.append(team)
        return new_list
    else:
        return league_team_based_on_position

def choose_a_team(nbnb):
    for i in range(len(data.country_of_the_team)):
        print(f"{i+1}. {data.country_of_the_team[i]}")
    print()
    print()
    country_nb = input(f"Country of Team {nbnb} (choose between 1 and {len(data.country_of_the_team)}): ")
    check_data_entered_is_good(country_nb , len(data.country_of_the_team))

    inputError = 0
    specialInput = False
    #league_team_based_on_position = get_team_of_a_league(S,int(country_nb) - 1)
    league_team_based_on_position = same_name_team_check(get_team_of_a_league(S,int(country_nb) - 1),country_nb)
    if len(league_team_based_on_position) > 0:
        for i in range(len(league_team_based_on_position)):
            if len(league_team_based_on_position) > 1:
                print(f"{i + 1}. {league_team_based_on_position[i]}")

    else:    
        #IN CASE MY CODE IS BAD

        for i in range(len(data.allTeam_[int(country_nb) - 1])):
            if len(data.allTeam_[int(country_nb) - 1][0].strip()) > 1:
                print(f"{i + 1}. {data.allTeam_[int(country_nb) - 1][i].strip()}")    
                specialInput = True
            elif len(data.allTeam_[int(country_nb) - 1][i].strip()) > 1:
                print(f"{i}. {data.allTeam_[int(country_nb) - 1][i].strip()}")
            else:
                inputError+=1

    team_nb = input(f"Choose your team (choose between 1 and {len(league_team_based_on_position)}): ")
    team_nb = int(team_nb)

    # IN CASE MY CODE IS BAD

    if len(league_team_based_on_position) == 0:
        if specialInput == True:
            team_nb-=1
        check_data_entered_is_good(team_nb , len(data.allTeam_[int(country_nb) - 1]) - inputError)
        return data.allTeam_[int(country_nb) - 1][int(team_nb) - 1].strip()
    else:
        check_data_entered_is_good(team_nb,len(league_team_based_on_position))
        return league_team_based_on_position[team_nb - 1]
    

def calc_pourcent_of_win(nb1,nb2):
    try:
        return (round(nb1/(nb2/100),1))
    except:
        return 1


def player_out_from_starting_xi(starting_xi,player_out):

    player_out_from_the_starting_xi_list = []

    for player in player_out:
        if player in starting_xi:
            player_out_from_the_starting_xi_list.append(player)

    return player_out_from_the_starting_xi_list
    
    
def team_vs_team(team1,team2,nbOfGameToAnalyze,national=False):
    national_team_list = print_file_info("nationalTeam.txt").split("\n")
    national_team_list_in_alphabetic_order = print_file_info("nationalTeamAlphabeticOrder.txt").split("\n")

    if national == True:
        x = get_the_score_of_the_main_team(team1,int(nbOfGameToAnalyze),True,True,national_team_list.index(team1))
        y = get_the_score_of_the_main_team(team2,int(nbOfGameToAnalyze),True,True,national_team_list.index(team2))
    else:
        x = get_the_score_of_the_main_team(team1,int(nbOfGameToAnalyze),False)
        y = get_the_score_of_the_main_team(team2,int(nbOfGameToAnalyze),False)
    
    score_of_team1 = abs(x)
    if x > 0 and y < 0 :
        score_of_team1 += abs(y) * 2
    print("+"*200)
    score_of_team2 = abs(y)
    if x < 0 and y > 0:
        score_of_team2 += abs(x) * 2
    
    out_power = 25
    out_power_of_player = (out_power / 11)
    print(f"Score of {team1}: {score_of_team1} , Score of {team2}: {score_of_team2}")
    
    try:
        if national is False:
            player_out_team1 = get_unavaible_player_of_a_team(S,print_file_info("teamUrl.txt").lower().split("\n")[print_file_info("allteam.txt").lower().split("\n").index(team1.lower())],False)
            if "none" not in str(player_out_team1):
                team1_starting_xi = print_file_info("starting_xi_league_team.txt").lower().split("\n")[print_file_info("allteam.txt").lower().split("\n").index(team1.lower())]
                player_out_from_starting_xi_list = player_out_from_starting_xi(team1_starting_xi,player_out_team1)
                if len(player_out_from_starting_xi_list) > 0:
                    print("Before out player " , score_of_team1)
                    score_of_team1 = int(score_of_team1 * ((100 - (out_power_of_player * len(player_out_from_starting_xi_list)))/100))
                    print("After out player " , score_of_team1 , " list of out player " , player_out_from_starting_xi_list)
        else:
            player_out_team1 = get_unavaible_player_of_a_team(S,print_file_info("nationalTeamUrl.txt").lower().split("\n")[print_file_info("nationalTeam.txt").lower().split("\n").index(team1.lower())],True)
            if "none" not in str(player_out_team1):
                team1_starting_xi = print_file_info("starting_xi_national_team.txt").lower().split("\n")[print_file_info("nationalTeam.txt").lower().split("\n").index(team1.lower())]
                player_out_from_starting_xi_list = player_out_from_starting_xi(team1_starting_xi,player_out_team1)
                if len(player_out_from_starting_xi_list) > 0:
                    print("Before out player " , score_of_team1)
                    score_of_team1 = int(score_of_team1 * ((100 - (out_power_of_player * len(player_out_from_starting_xi_list)))/100))
                    print("After out player " , score_of_team1 , " list of out player " , player_out_from_starting_xi_list)
    except:
        pass    
    
    try:
        if national is False:
            player_out_team2 = get_unavaible_player_of_a_team(S,print_file_info("teamUrl.txt").lower().split("\n")[print_file_info("allteam.txt").lower().split("\n").index(team1.lower())],False)
            if "none" not in str(player_out_team1):
                team2_starting_xi = print_file_info("starting_xi_league_team.txt").lower().split("\n")[print_file_info("allteam.txt").lower().split("\n").index(team1.lower())]
                player_out_from_starting_xi_list = player_out_from_starting_xi(team2_starting_xi,player_out_team2)
                #print("Score Before out player " , score_of_team1)
                if len(player_out_from_starting_xi_list) > 0:
                    print("Before out player " , score_of_team2)
                    score_of_team2 = int(score_of_team1 * ((100 - (out_power_of_player * len(player_out_from_starting_xi_list)))/100))
                    print("After out player " , score_of_team2 , " list of out player " , player_out_from_starting_xi_list)
                #print("Score After out player " , score_of_team1 , " list of out player " , player_out_from_starting_xi_list)
        else:
            player_out_team1 = get_unavaible_player_of_a_team(S,print_file_info("nationalTeamUrl.txt").lower().split("\n")[print_file_info("nationalTeam.txt").lower().split("\n").index(team1.lower())],True)
            if "none" not in str(player_out_team1):
                team2_starting_xi = print_file_info("starting_xi_national_team.txt").lower().split("\n")[print_file_info("nationalTeam.txt").lower().split("\n").index(team1.lower())]
                player_out_from_starting_xi_list = player_out_from_starting_xi(team2_starting_xi,player_out_team2)
                if len(player_out_from_starting_xi_list) > 0:
                    print("Before out player " , score_of_team2)
                    score_of_team2 = int(score_of_team1 * ((100 - (out_power_of_player * len(player_out_from_starting_xi_list)))/100))
                    print("After out player " , score_of_team2 , " list of out player " , player_out_from_starting_xi_list)      
    except:
        pass    
    
    #player_out_team1 = get_unavaible_player_of_a_team(S,team_url,False)

    if score_of_team1 > score_of_team2:
        if score_of_team2 * 1.25 < score_of_team1:
            print(f"{team2} will loose against {team1}")
        else:
            print(f"{team1} have a win ratio a little bit higher than {team2} but the most likely outcome is a draw")
        print(f"{team1} have a win rate of {calc_pourcent_of_win(score_of_team1,score_of_team1+score_of_team2)} against {team2}")
        print(f"{team2} have a win rate of {calc_pourcent_of_win(score_of_team2,score_of_team1+score_of_team2)} against {team1}")
        
    else:
        if score_of_team1 * 1.25 < score_of_team2:
            print(f"{team1} will loose against {team2}")
        else:
            print(f"{team2} have a win ratio a little bit higher than {team1} but the most likely outcome is a draw")
        print(f"{team2} have a win rate of {calc_pourcent_of_win(score_of_team2,score_of_team1+score_of_team2)} against {team1}")
        print(f"{team1} have a win rate of {calc_pourcent_of_win(score_of_team1,score_of_team1+score_of_team2)} against {team2}")

reset_file("ckk.txt")
choose = input(f"1. National Team \n2. League team \n3. Exit\n:")
check_data_entered_is_good(choose,3)

if int(choose) == 1:
    print("national gang")

    national_team_list = print_file_info("nationalTeam.txt").split("\n")
    national_team_list_in_alphabetic_order = print_file_info("nationalTeamAlphabeticOrder.txt").split("\n")
    
    chooose = input(f"1. Team VS Team \n2. Stat of a team \n3. Exit\n:")
    check_data_entered_is_good(chooose,3)

    if int(chooose) == 2:
        for i in range(len(national_team_list_in_alphabetic_order)):
            print(f"{i + 1} {national_team_list_in_alphabetic_order[i]}")
        
        team_nb = int(input(f"Choose your team (choose between 1 and {len(national_team_list_in_alphabetic_order)}): ")) - 1
        
        team1 = national_team_list_in_alphabetic_order[team_nb] 
        get_the_score_of_the_main_team(team1,999,True,True,national_team_list.index(national_team_list_in_alphabetic_order[team_nb]))

    if int(chooose) == 1:
        for i in range(len(national_team_list_in_alphabetic_order)):
            print(f"{i + 1} {national_team_list_in_alphabetic_order[i]}")
        
        team_nb = int(input(f"Choose your team (choose between 1 and {len(national_team_list_in_alphabetic_order)}): ")) - 1

        
        team1 = national_team_list_in_alphabetic_order[team_nb] 
        #get_the_score_of_the_main_team(team1,20,False,True,national_team_list.index(national_team_list_in_alphabetic_order[team_nb]))
        
        for i in range(len(national_team_list_in_alphabetic_order)):
            print(f"{i + 1} {national_team_list_in_alphabetic_order[i]}")
        
        team_nb = int(input(f"Choose your team (choose between 1 and {len(national_team_list_in_alphabetic_order)}): ")) - 1

        team2 = national_team_list_in_alphabetic_order[team_nb]
        nbOfGameToAnalyze = input("How many games to you want the bot to analyze? (Min 1 Max 20)" + "\n" + "The bigger the number is the better the analyze will be:")
        team_vs_team(team1,team2,nbOfGameToAnalyze,True)
    
elif int(choose) == 2:
    chooose = input(f"1. Team VS Team \n2. Stat of a team \n3. Exit\n:")
    check_data_entered_is_good(chooose,3)

    if int(chooose) == 2:
        team1 = choose_a_team(1).replace(" ","-")
        get_the_score_of_the_main_team(team1,999,True)

    elif int(chooose) == 1:
        team1 = choose_a_team(1).replace(" ","-")
        team2 = choose_a_team(2).replace(" ","-")

        nbOfGameToAnalyze = input("How many games to you want the bot to analyze? (Min 1 Max 20)" + "\n" + "The bigger the number is the better the analyze will be:")
        check_data_entered_is_good(nbOfGameToAnalyze,20)
        #nbOfGameToAnalyze = 20
        print(f"{team1} vs {team2}")
        team_vs_team(team1,team2,nbOfGameToAnalyze)
        
    else:
        print("Good Bye")
        quit()
else:
    print("Good bye")
    quit()