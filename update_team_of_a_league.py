from scrapData import add_new_team , Scraper , teamData , get_national_team_list , get_team_of_a_league, get_url_of_national_team , accept_cookie

from printData import write_into_file , reset_file , print_file_info
import time
S = Scraper()
data = teamData()


# print(data.all_league_url)
# print(data.allTeam_)
# print(data.country_of_the_team)

reset_file("updated_team.txt")
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

country_nb = 1
def update_team():
    for country , team , url in zip(data.country_of_the_team,data.allTeam_,data.all_league_url):
        #print(country,team,url)

        league_team_based_on_position = same_name_team_check(get_team_of_a_league(S,int(country_nb) - 1),country_nb)
        team.sort()
        team = team[2:]
        league_team_based_on_position.sort()
        #print(team,league_team_based_on_position)
        team_new_in_list = []
        team_bad_in_list = []
        
        team1_list = []
        team2_list = []
        
        for team1 , team2 in zip(team,league_team_based_on_position):
            team1 = team1.replace("    ","")
            team2 = team2.replace("-" ," ")
            team1_list.append(team1)
            team2_list.append(team2)
        
        for t1 , t2 in zip(team1_list,team2_list):
            if t1 not in team2_list:
                team_bad_in_list.append(t1)
            if t2 not in team1_list:
                team_new_in_list.append(t2)
            

        print(country)
        print("Out of the league: " , team_bad_in_list)
        print("New to the league: ", team_new_in_list)
        print("-"*20)
        
        write_into_file("updated_team.txt",str(country)+"\n")
        write_into_file("updated_team.txt",str(team_bad_in_list)+"\n")
        write_into_file("updated_team.txt",str(team_new_in_list)+"\n")
        write_into_file("updated_team.txt","-"*20+"\n")
        
        time.sleep(5)
        country_nb+=1

def add_new_team_to_data():
    print("yooooh")
    index = 1
    for url in data.all_league_url:
        add_new_team(S,url)
        time.sleep(0.1)

def add_national_team():
    get_national_team_list(S)

def add_national_team_url():
    allTeam = print_file_info("nationalTeam.txt").split("\n")
    allTeamUrlList = []
    for team in allTeam:
        fake,teamUrl = get_url_of_national_team(S,team)
        if fake == True:
            allTeamUrlList.append(teamUrl)
        else:
            allTeamUrlList.append("flop "+ team + " flop")
            print("Flop: " , team)
    print(allTeamUrlList)

S = Scraper()
data = teamData()
reset_file("ckk.txt")
S.driver.get("https://www.footmercato.net/club/real-madrid/")
time.sleep(2)
accept_cookie(S)
add_new_team_to_data()
