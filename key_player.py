from printData import write_into_file , reset_file , print_file_info
import time
from scrapData import * 

def get_key_player_league():
    S = Scraper()
    data = teamData()
    reset_file("ckk.txt")
    S.driver.get("https://www.footmercato.net/club/real-madrid/")
    time.sleep(2)
    accept_cookie(S)
    time.sleep(10)
    all_team = print_file_info("teamUrl.txt").split("\n")
    for  i , team_url in enumerate(all_team):
        if i < 186:
            continue
        x = get_starting_xi_of_a_team(S,team_url)
        write_into_file("starting_xi_league_team.txt",x)
        write_into_file("starting_xi_league_team.txt","\n")

        print(x,i)
        time.sleep(3)

def get_key_player_national():
    S = Scraper()
    data = teamData()
    reset_file("ckk.txt")
    S.driver.get("https://www.footmercato.net/club/real-madrid/")
    time.sleep(2)
    accept_cookie(S)
    time.sleep(10)
    all_team = print_file_info("nationalTeamUrl.txt").split("\n")
    for i , team_url in enumerate(all_team):
        x = get_starting_xi_of_a_team(S,team_url,True)
        write_into_file("starting_xi_national_team.txt",x)
        write_into_file("starting_xi_national_team.txt","\n")
        print(x,i)
        time.sleep(3)

#get_key_player_national()
#get_key_player_league()