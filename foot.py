from scrapData import * 
from teamData import *
S = Scraper()




def last_X_Games_Result(listOfResult):
    team =  stats.name
    win,draw,loose = 0,0,0
    totalOfGame = len(listOfResult)
    
    for result in listOfResult:
        result = result.split()
        if (team in result[0] and int(result[1]) > int(result[3])) or (team in result[2] and int(result[3]) > int(result[1])):
            win+=1
            if team in result[0]:
                stats.last_x_game_win.append(result[0]+"_"+result[2])
                stats.last_x_game_win_score.append(result[1]+"_"+result[3])
                stats.nb_of_goal_scored+=int(result[1])
                stats.nb_of_goal_conceded+=int(result[3])
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
                stats.last_x_game_win.append(result[2]+"_"+result[0])
                stats.last_x_game_win_score.append(result[3]+"_"+result[1])
                stats.nb_of_goal_scored+=int(result[3])
                stats.nb_of_goal_conceded+=int(result[1])
                stats.last_x_game_list.append(result[2]+"_"+result[0])
                stats.last_x_game_list_score.append(result[3]+"_"+result[1])
                res = pos_league_team(result[0])
                if res == -1:
                    stats.last_x_game_list_league_or_not.append("X")
                    stats.last_x_game_draw_league_or_not.append("X")
                else:
                    if stats.league_of_the_team == data.all_league_name[res]:
                        stats.last_x_game_list_league_or_not.append("L")
                        stats.last_x_game_win_league_or_not.append("L")
                    else:
                        stats.last_x_game_list_league_or_not.append("N")
                        stats.last_x_game_win_league_or_not.append("N")
        elif (int(result[1]) == int(result[3])):
            if team in result[0]:
                stats.last_x_game_draw.append(result[0]+"_"+result[2])
                stats.last_x_game_draw_score.append(result[1]+"_"+result[3])
                stats.nb_of_goal_scored+=int(result[1])
                stats.nb_of_goal_conceded+=int(result[3])
                stats.last_x_game_list.append(result[0]+"_"+result[2])
                stats.last_x_game_list_score.append(result[1]+"_"+result[3])
                res = pos_league_team(result[2])
                if res == -1:
                    stats.last_x_game_list_league_or_not.append("X")
                    stats.last_x_game_loose_league_or_not.append("X")
                else:
                    if stats.league_of_the_team == data.all_league_name[res]:
                        stats.last_x_game_list_league_or_not.append("L")
                        stats.last_x_game_draw_league_or_not.append("L")
                    else:
                        stats.last_x_game_list_league_or_not.append("N")
                        stats.last_x_game_draw_league_or_not.append("N")

            else:
                stats.last_x_game_draw.append(result[2]+"_"+result[0])
                stats.last_x_game_draw_score.append(result[3]+"_"+result[1])
                stats.nb_of_goal_scored+=int(result[3])
                stats.nb_of_goal_conceded+=int(result[1])
                stats.last_x_game_list.append(result[2]+"_"+result[0])
                stats.last_x_game_list_score.append(result[3]+"_"+result[1])
                res = pos_league_team(result[0])
                if res == -1:
                    stats.last_x_game_list_league_or_not.append("X")
                    stats.last_x_game_win_league_or_not.append("X")
                else:
                    if stats.league_of_the_team == data.all_league_name[res]:
                        stats.last_x_game_list_league_or_not.append("L")
                        stats.last_x_game_draw_league_or_not.append("L")
                    else:
                        stats.last_x_game_list_league_or_not.append("N")
                        stats.last_x_game_draw_league_or_not.append("N")
            

            draw+=1
        else:
            if team in result[0]:
                stats.last_x_game_loose.append(result[0]+"_"+result[2])
                stats.last_x_game_loose_score.append(result[1]+"_"+result[3])
                stats.nb_of_goal_scored+=int(result[1])
                stats.nb_of_goal_conceded+=int(result[3])
                stats.last_x_game_list.append(result[0]+"_"+result[2])
                stats.last_x_game_list_score.append(result[1]+"_"+result[3])
                res = pos_league_team(result[2])
                if res == -1:
                    stats.last_x_game_list_league_or_not.append("X")
                    stats.last_x_game_win_league_or_not.append("X")
                else:    
                    if stats.league_of_the_team == data.all_league_name[res]:
                        stats.last_x_game_list_league_or_not.append("L")
                        stats.last_x_game_loose_league_or_not.append("L")
                    else:
                        stats.last_x_game_list_league_or_not.append("N")
                        stats.last_x_game_loose_league_or_not.append("N")

            else:
                stats.last_x_game_loose.append(result[2]+"_"+result[0])
                stats.last_x_game_loose_score.append(result[3]+"_"+result[1])
                stats.nb_of_goal_scored+=int(result[3])
                stats.nb_of_goal_conceded+=int(result[1])
                stats.last_x_game_list.append(result[2]+"_"+result[0])
                stats.last_x_game_list_score.append(result[3]+"_"+result[1])
                res = pos_league_team(result[0])
                if res == -1:
                    stats.last_x_game_list_league_or_not.append("X")
                    stats.last_x_game_win_league_or_not.append("X")
                else:
                    if stats.league_of_the_team == data.all_league_name[res]:
                        stats.last_x_game_list_league_or_not.append("L")
                        stats.last_x_game_draw_league_or_not.append("L")
                    else:
                        stats.last_x_game_list_league_or_not.append("N")
                        stats.last_x_game_draw_league_or_not.append("N")
            
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
    
    # print(stats.last_x_game_win)
    # print(stats.last_x_game_win_score)
    # print(stats.last_x_game_draw)
    # print(stats.last_x_game_draw_score)
    # print(stats.last_x_game_loose)
    # print(stats.last_x_game_loose_score)
    # print(stats.nb_of_goal_scored)
    # print(stats.nb_of_goal_scored_per_match)
    # print(stats.nb_of_goal_conceded)
    # print(stats.nb_of_goal_conceded_per_match)
    # print(stats.nb_of_game)
    
    #print(f"Win {win} {int((win/totalOfGame) * 100)}  %  Draw {draw} {int((draw/totalOfGame) * 100)} %  Loose {loose} {int((loose/totalOfGame) * 100)} %  Total games {totalOfGame}")
    return

def print_all_data():
    print(f"Team Name: {stats.name}")
    print(f"Points: {stats.point}")
    print(f"Position in the League: {stats.pos_on_the_league}")
    print(f"League of the Team: {stats.league_of_the_team}")
    print(f"Last {len(stats.last_x_game_list)} Games: {stats.last_x_game_list}")
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
        

    
data = teamData()
stats = TeamStat()
#stats.name = "man-city"
stats.name = "montpellier"

stats.name = stats.name.lower()

if stats.name not in data.allTeam:
    print("team not in the team data")
    exit()

stats.pos_on_the_league = Position_Of_A_Team_On_Its_League(S,stats.name)
data.pos_league_team = pos_league_team(stats.name)
stats.league_of_the_team = data.all_league_name[data.pos_league_team]
# print("Team Name " , stats.name)
# print("League name " , data.all_league_name[data.pos_league_team])
# print("Position on the league " , stats.pos_on_the_league)
# print("Country " , data.country_of_the_team[data.pos_league_team])
allTeamTxt = print_file_info("allteam.txt").split("\n")
team_pos = allTeamTxt.index(stats.name)
last_X_Games_Result(Get_Last_X_Games_Result(S,stats.name,team_pos))
#print(vars(stats))

print_all_data()