from random import randint

import requests
from os import system

import pickle
from selenium.webdriver.common.action_chains import ActionChains

from teamData import *
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from os import system
import time

from datetime import datetime, timedelta
import os.path
from datetime import datetime, timedelta
from datetime import date

import os

from teamData import *

def print_pkl_info():
    try:
        file_path = f"cookies{0}.pkl"
        with open(file_path, 'rb') as file:
            try:
                data = pickle.load(file)
            except:
                return ""
        return (data)
    except:
        return ("")

class Scraper:
    
    wait_time = 5
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=1')
    options.add_argument("--log-level=3")  # Suppress all logging levels
    
    if len(str(print_pkl_info())) > 20:
        options.add_argument('headless')
    
    #options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument("--disable-gpu")  # Disable GPU (helpful in headless mode)
    options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(15)
    
class SZcraper:
    def __init__(self, headless=True):
        self.wait_time = 5
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--log-level=1')
        self.options.add_argument('--log-level=3')  # Suppress all logging levels
        # self.options.add_argument('--blink-settings=imagesEnabled=false')

        # Set headless mode based on the parameter
        if headless:
            self.options.add_argument('--headless')
        
        self.options.add_argument('--disable-gpu')  # Disable GPU (helpful in headless mode)
        self.options.add_argument('--disable-dev-shm-usage')  # Prevent shared memory issues

        # Initialize the WebDriver
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.set_page_load_timeout(15)

def accept_cookie(S,stop=False):

    #time.sleep(1000)

    if print_file_info("ckk.txt") == "1":
        return
    time.sleep(1)
    try:
        try:
            ck = print_pkl_info()
        except:
            ck = ""
        
        ck = ""
        if len(str(ck)) > 20:
            cookies = pickle.load(open(f"cookies{0}.pkl","rb"))
            for cookie in cookies:
                S.driver.add_cookie(cookie)
            write_into_file("ckk.txt",1)
            
        else:
            reset_file("ckk.txt")
            acceptBtnXpath = "/html/body/div[1]/div/div/div/div/div/div[2]/button[1]"
            acceptBtnID = "didomi-notice-agree-button"
            element = WebDriverWait(S.driver,3).until(
            EC.presence_of_element_located((By.ID, acceptBtnID)))

            element.click()
            pickle.dump(S.driver.get_cookies(), open(f"cookies{0}.pkl", "wb"))
            write_into_file("ckk.txt",1)

    except:
        import traceback
        # if stop == True:
        #     print("too much error bye")
        #     exit() 
        # print("coockie flop")
        # reset_file("ckk.txt")   
        # accept_cookie(S,True)
        pass  
  

def is_num(nb):
    try:
        int(nb)
        return True
    except:
        return False
 
def remove_first_two_elem(str):
    words = str.split()
    if len(words) < 2:
        return str
    unique_words = words[2:]
    return ' '.join(unique_words)

def isSlash(string):
    letter = "abcdefghijklmnopqrstuvwxyz"
    if "/" not in string:
        return False
    
    for char in string:
        if char in letter:
            return False

    return True

def checkNum(string):
    string = string.strip().split(" ")
    if len(string) < 4:
        return False
    if is_num(string[1]) == True and is_num(string[3]) == True:
        return True
    return False

def get_url_of_a_team(posTeam):
    try:
        all_url = print_file_info("teamUrl.txt").split("\n")
        return all_url[posTeam]
    except:
        return("")

def get_match_of_the_day(S):
    try:
        allTeam = print_file_info("allteam.txt").lower().split("\n")
        allTeamNational = print_file_info("nationalTeam.txt").lower().split("\n")
        try:
            dayNb = int(print_file_info("dayNb.txt"))
        except:
            dayNb = 1
        if dayNb < 0:
            dayNb = 0
        current_date = datetime.now()
        next_day = current_date + timedelta(days=dayNb)
        formatted_next_day = next_day.strftime("%Y-%m-%d")

        S.driver.get(f"https://www.footmercato.net/live/{formatted_next_day}")
        time.sleep(5)
        accept_cookie(S)
        #S.driver.get(f"https://www.footmercato.net/live/")

        page_text = S.driver.find_element(By.TAG_NAME, "body").text
        #print(page_text)
        #print("-"*200)
        skipMatches = page_text.split("Amicaux Club")
        skipMatches2 = page_text.split("Amicaux (femmes)")
        skipMatches3 = page_text.split("Serie C")

        list_of_matches = []
        error = 0
        skip = False
        for j in range(3,60):
            for i in range(1,60):
                try:
                    test = f"/html/body/div[4]/div[3]/div/div[1]/div[{j}]/div[2]/div[{i}]/div"
                    #test = f"/html/body/div[4]/div[3]/div/div[1]/div[3]/div[2]/div[1]/div/a/span[1]"
                    element = WebDriverWait(S.driver,3).until(
                    EC.presence_of_element_located((By.XPATH, test)))
                    #print(element.text ,  " a ")
                    matches = element.text.replace(" ","-").split("\n")
                    if len(skipMatches) > 1:
                        if element.text in skipMatches[1]:
                            skip = True
                    
                    if len(skipMatches2) > 1:
                        if element.text in skipMatches2[1]:
                            skip = True
                    
                    if len(skipMatches3) > 1:
                        if element.text in skipMatches3[1]:
                            skip = True
                    
                    if ((matches[0].lower() in allTeam and matches[1].lower() in allTeam) or (matches[0].lower() in allTeamNational and matches[1].lower() in allTeamNational)) and skip != True:
                        list_of_matches.append(matches[0] + "#####" + matches[1])
                    
                    error = 0
                except:
                    import traceback
                    # traceback.print_exc()
                    # print(j,i)
                    
                    error+=1
                    if error > 5:
                        return list_of_matches
                    break
        return list_of_matches
    except:
        import traceback
        traceback.print_exc()

def get_head_to_head_result_of_two_teams(S,posTeam,team,team2):
    try:
        team = team.replace("-"," ")
        team2 = team2.replace("-"," ")
        
        team = team.lower()
        team2 = team2.lower()
        all_url = print_file_info("teamUrl.txt").split("\n")
        national_team_list = print_file_info("nationalTeam.txt").lower().split("\n")
        national_team_list_url = print_file_info("nationalTeamUrl.txt").lower().split("\n")
        reverse =  False
        S.driver.get(f"{all_url[posTeam]}calendrier/#tabPlayed")
        
        matchs_url = WebDriverWait(S.driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "matchFull__link")))

        matchs_team_name = WebDriverWait(S.driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "matchFull__teams")))
        

        matchs_team_name = WebDriverWait(S.driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "matchFull__teams")))


        index = 0
        skipSearch = False
        for url , name in zip(matchs_url,matchs_team_name):
            if team2.lower() in name.text.lower().replace("-"," "):
                skipSearch = True
                skipSearch = True
                try:
                    matchs_url[index].click()
                except:
                    pass
                time.sleep(5)
                break
            index += 1
        
        if skipSearch is False:
            S.driver.get(f"{all_url[posTeam]}calendrier")            
            matchs_url = WebDriverWait(S.driver,15).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "matchFull__link")))

            matchs_team_name = WebDriverWait(S.driver,15).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "matchFull__teams")))

            

            index = 0
            skipSearch = False
            for url , name in zip(matchs_url,matchs_team_name):
                if team2.lower() in name.text.lower().replace("-"," "):
                    skipSearch = True
                    try:
                        matchs_url[index].click()
                    except:
                        pass
                    break
                index += 1
        
        
        try:
            t1_name = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[3]/div/div[2]/div[2]/div/a[1]/span[2]")))
        except:
            t1_name = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "scoreboard__teamName")))
            
        all_game_url = print_file_info("all_game_url.txt").lower().split("\n")
        if S.driver.current_url.lower() not in all_game_url:
            write_into_file("all_game_url.txt",S.driver.current_url+"\n")

        write_into_file("recent_game_url.txt",S.driver.current_url+"\n")
        if team.replace("-"," ").strip().lower() == t1_name.text.replace("-"," ").strip().lower():
            reverse = True
        
        try:
            element = WebDriverWait(S.driver,2).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "verticalPercentageBar__legend")))
        except:
            return 0

        nb_win = int(element[0].text.split(" ")[0])
        nb_draw = int(element[1].text.split(" ")[0])
        nb_loose = int(element[2].text.split(" ")[0])
    
        
        total = nb_win + nb_draw + nb_loose
        nb_win = nb_win + nb_draw/2
        nb_loose = nb_loose + nb_draw/2
        try:
            pourcent_win = (nb_win/total)*100
        except:
            pourcent_win = 1
        
        try:
            pourcent_loose = (nb_loose/total)*100
        except:
            pourcent_loose = 1
        # print(nb_win,pourcent_win)
        # print(nb_loose,pourcent_loose)
        
        if (pourcent_win < 60 and pourcent_win > 40) or (pourcent_loose < 60 and pourcent_loose > 40):
            return 0
        
        if nb_win == 0:
            return 20
        
        if nb_loose == 0:
            return -20
        
        # 1.5 to 100
        # 5% to 20%
        percent_start = 5
        if pourcent_loose < pourcent_win:
            pourcent_win = (nb_win/total)*100
            pourcent_loose = (nb_loose/total)*100
            if reverse == False:
                return  - (percent_start + ((pourcent_win - 60)*0.375))
            
            return  (percent_start + ((pourcent_win - 60)*0.375))
        else:
            pourcent_win = (nb_win/total)*100
            pourcent_loose = (nb_loose/total)*100
            if reverse == False:
                return  (percent_start + ((pourcent_loose - 60)*0.375))        
            return  -(percent_start + ((pourcent_loose - 60)*0.375))        
    except:
                    
        #print(f"flopppp {team},{team2} {posTeam}")
        return 0


def Get_Last_X_Games_Result(S,team,posTeam,nbOfGameToAnalyze=20,National=False):
    
    try:
        years = ["2024","2025","2026"]
        all_url = print_file_info("teamUrl.txt").split("\n")
        #S.driver.get(all_url[posTeam])

        if National == True:
            accept_cookie(S)

        #time.sleep(5)
        national_team_list = print_file_info("nationalTeam.txt").lower().split("\n")
        national_team_list_url = print_file_info("nationalTeamUrl.txt").lower().split("\n")
        
        if National == False:
            S.driver.get(f"{all_url[posTeam]}calendrier/#tabPlayed")
        else:
            S.driver.get(f"{national_team_list_url[national_team_list.index(team)]}/#tabPlayed")
        lastResultXpath = "/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/nav/a[2]"
        
        calendarXpath = "/html/body/div[3]/div[4]/div/div/nav/ul/li[4]/a"

        tabResultXpath = "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div"

        element = WebDriverWait(S.driver,15).until(
        EC.presence_of_element_located((By.XPATH, tabResultXpath)))

        listOfResult = []
        lastXmatch = element.text
        lastXmatchSplit = lastXmatch.split("\n")
        index = 1
        string = ""
        first = True
        team = team.lower()
        change = False
        
        for i in range(len(lastXmatchSplit)):
            if "2022" in lastXmatchSplit[i] or "2023" in lastXmatchSplit[i] or "2024" in lastXmatchSplit[i] or "2025" in lastXmatchSplit[i] or "2026" in lastXmatchSplit[i] or "terminé" in lastXmatchSplit[i].lower() or isSlash(lastXmatchSplit[i].lower()) == True:
                continue
            else:
                if is_num(lastXmatchSplit[i].replace(" ","-")) == False and lastXmatchSplit[i].replace(" ","-") in string:
                    string+= remove_first_two_elem(lastXmatchSplit[i].replace(" ","-")) + " "
                    #print("dzdzd " ,  remove_first_two_elem(lastXmatchSplit[i].replace(" ","-")))
                else:
                    string+= lastXmatchSplit[i].replace(" ","-") + " "
                if index % 4 == 0 and index > 0:
                    checkStr = string.split(" ")
                    notNb = 0
                    lst = []
                    for str in checkStr:
                        if len(lst) > 4:
                            lst = []
                            break
                        if is_num(str) == False:
                            notNb+=1
                            lst.append(str.lower())
                        else:
                            notNb = 0
                        if notNb == 2:
                            index-=1
                            change = True
                        
                        if notNb == 3:
                            string = string.lower().replace(lst[0],"",1).replace(lst[1],"",1)
                            index-=1
                            change = True
                        
                    lst = []
                    digit_count = sum(char.isdigit() for char in string.strip().lower())
                    if index == 4 or (change == True and index == 2) and len(string.split()) == 4 and "/" not in string.strip().lower():
                        #print("on est al " , string.strip().lower())
                        if checkNum(string.strip().lower()) == True:
                            listOfResult.append(string.strip().lower())
                        string = ""
                        change = False
                        index = 0
                if len(listOfResult) >= nbOfGameToAnalyze:
                    break
                #print("dendex " , index)
                index+=1
        if len(listOfResult) == 0:
            return []
        if len(listOfResult) > 20:
            listOfResult = listOfResult[0:20]
        return listOfResult
    except:
        return []


def has_Team_Played_since_september(S,team,posTeam):
    
    try:
        all_url = print_file_info("teamUrl.txt").split("\n")
        S.driver.get(f"{all_url[posTeam]}calendrier/#tabPlayed")
        tabResultXpath = "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div"
        try:
            element = WebDriverWait(S.driver,15).until(
            EC.presence_of_element_located((By.XPATH, tabResultXpath)))
        except:
            return False
        year = int(element.text.split(" ")[1])
        month = element.text.split(" ")[0]
        good_month = ["septembre","octobre","novembre","décembre"]
        time.sleep(5)
        if year >= int(date.today().year) or (year == 2024 and month.lower() in good_month):
            print(f"Last gamed played by {team}: " , element.text)
            return True
        if month.lower() not in good_month:
            print(f"Last gamed played by {team}: " , element.text)
            print("Team didnt played recently skiiping this game")    
            return False
        
        print(f"Last gamed played by {team}: " , element.text)
        print("Team didnt played recently skiiping this game")    

        return False
    except:
        return True    

def add_days_to_date(days_to_add):
    # Get the current date
    date_obj = datetime.today()
    
    # Add the specified number of days
    new_date_obj = date_obj + timedelta(days=days_to_add)
    
    # Convert back to string in the same format
    new_date_str = new_date_obj.strftime("%d/%m/%Y")
    
    return new_date_str


def doesMatchHaveOdds(S,team1,team2,otherSearch=False):
    try:
        if otherSearch == True:
            S.driver.get(f"https://www.bing.com/search?q={team1}+{team2}+pronostic&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ok&sc=8-2&sk=&cvid=D452EBD3F49940C8A8A329E281AD7C4F&ghsh=0&ghacc=0&ghpl=")
        else:
            S.driver.get(f"https://www.bing.com/search?q={team1}+{team2}+cote&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ok&sc=8-2&sk=&cvid=D452EBD3F49940C8A8A329E281AD7C4F&ghsh=0&ghacc=0&ghpl=")
        S.driver.execute_script("document.body.style.zoom='50%'")
        links = S.driver.find_elements(By.TAG_NAME, "a")
        time.sleep(5)
        if otherSearch == True:
            time.sleep(15)
        
        all_links = [link.get_attribute("href") for link in links]
        linkToGo = ""
        for link in all_links:
            if link:  # Check if the href is not None
                if "sportytrader.com" in link:
                    linkToGo = link
                    break
        if linkToGo == "":
            return False

        S.driver.get(linkToGo)
        S.driver.execute_script("document.body.style.zoom='30%'")

        return True

        if otherSearch == True:
            time.sleep(15)
        tableCote = "/html/body/div[1]/div[2]/div[4]/section/main/section[2]/div[1]/div/table/tbody/tr[1]"
        
        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, tableCote)))
        #print("La cooteee " , odds)
        return True
    except:
        # import traceback
        # traceback.print_exc()
        # print(team1,team2)
        return False

def check_split(str1,str2):
    try:
        str1 = str1.split("-")
        for s in str1:
            if s in str2:
                return True
    except:
        return False

def get_odds(S,team1,team2,result,FirstResultOdd=False,TestDate=""):
    now = datetime.now()
    months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    current_day_number = now.day
    current_year = now.year  # Year (e.g., 2025)
    current_month = now.month

    try:
        team1=team1.lower()
        team2=team2.lower()
        if FirstResultOdd == False:
            try:
                S.driver.get(f"https://www.bing.com/search?q={team1}+{team2}+sporty+trader+&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ok&sc=8-2&sk=&cvid=D452EBD3F49940C8A8A329E281AD7C4F&ghsh=0&ghacc=0&ghpl=")
            except:
                time.sleep(10)
                S.driver.get(f"https://www.bing.com/search?q={team1}+{team2}+sporty+trader+cote {str(current_day_number)}+{months[current_month - 1]}+{str(current_year)}+&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ok&sc=8-2&sk=&cvid=D452EBD3F49940C8A8A329E281AD7C4F&ghsh=0&ghacc=0&ghpl=")        
        else:
            S.driver.get(f"https://www.bing.com/search?q={team1}+{team2}+sporty+trader+cote {str(current_day_number)}+{months[current_month - 1]}+{str(current_year)}+&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ok&sc=8-2&sk=&cvid=D452EBD3F49940C8A8A329E281AD7C4F&ghsh=0&ghacc=0&ghpl=")
        S.driver.execute_script("document.body.style.zoom='50%'")
        time.sleep(15)
        
        try:
            btnID = "bnp_btn_accept"
            btnXPATH = "/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/button[1]"
            element = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.XPATH, btnXPATH)))
            element.click()
            time.sleep(2)
        except:
            pass

        try:
            btnID = "bnp_btn_accept"
            btnXPATH = "/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/button[1]"
            element = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.ID, btnID)))
            element.click()
            time.sleep(2)
        except:
            pass
        
        links = S.driver.find_elements(By.TAG_NAME, "a")

        all_links = [link.get_attribute("href") for link in links]
        linkToGo = ""
        for link in all_links:
            if link:  # Check if the href is not None
                if ".sportytrader." in link and "us/picks" not in link and "com/pronostics/football/" not in link:
                    linkToGo = link
                    break

        S.driver.get(linkToGo)
        S.driver.execute_script("document.body.style.zoom='30%'")
        page_text = S.driver.find_element("tag name", "body").text
        daTe = add_days_to_date(int(print_file_info("dayNb.txt")))
        if len(TestDate) > 3:
            daTe = "01/02/2025"
        t1Name = page_text.split(daTe)[0].split("\n")[-2].lower()
        try:
            t2Name = page_text.split(daTe)[1].split("\n")[2].lower()
        except:
            t2Name = team2

        reverse = False
        if t2Name in team1 or team1 in t2Name or team1 == t2Name or check_split(team1,t2Name) == True:
            reverse = True
            #print("reeeveeeerseeeeee " , team1 , team2)
          
        if t1Name in team2 or team2 in t1Name or team2 == t1Name or check_split(team2,t1Name) == True:
            reverse = True
            #print("reeeveeeerseeeeee " , team1 , team2)
        
        if team1 in team2 or team2 in team1:
            #print("both team have a commun name " , team1,team2)
            reverse = False
        
        t1Name=t1Name.lower()
        t2Name=t2Name.lower()
        page_text = S.driver.find_element("tag name", "body").text.replace("\n"," ")
        #write_into_file("toto.txt",S.driver.find_element("tag name", "body").text)
        if "BOOKMAKER 1 X 2 BONUS" in page_text:
            pt = page_text.split("BOOKMAKER 1 X 2 BONUS")[1].split(" ")
            odds = pt[1] + "\n" + pt[2] + "\n" + pt[3] + "\n"
        elif "BOOKMAKER 1 N 2 BONUS" in page_text:
            pt = page_text.split("BOOKMAKER 1 N 2 BONUS")[1].split(" ")
            odds = pt[1] + "\n" + pt[2] + "\n" + pt[3] + "\n"
        else:
            try:
                pt = page_text.split(t2Name)[1].split(" ")
                odds = pt[1] + "\n" + pt[2] + "\n" + pt[3] + "\n"    
            except:
                pt = S.driver.find_element("tag name", "body").text.split(daTe)[1].split("\n")
                odds = pt[4] + "\n" + pt[6] + "\n" + pt[8] + "\n"        

        odds = odds.split("\n")
        #print("oooodddddssssss " , odds)
        
        odds1,odds2,odds3 = odds[0],odds[1],odds[2]
        if result == "W":
            odds = odds1
            if reverse == True:
                odds = odds3
            return odds
        if result == "D":
            odds = odds2
            return odds
        if result == "L":
            odds = odds3
            if reverse == True:
                odds = odds1
            return odds
        #print("La cooteee " , odds)
        return "-999"
    except:
        # if FirstResultOdd == True:
        #     import traceback
        #     traceback.print_exc()

        #     print(f"flop 2 {team1} vs {team2}")
        #     if FirstResultOdd == False:
        #         print(f"https://www.bing.com/search?q={team1}+{team2}+sporty+trader+pronostic&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ok&sc=8-2&sk=&cvid=D452EBD3F49940C8A8A329E281AD7C4F&ghsh=0&ghacc=0&ghpl=")
        #     else:
        #         print(f"https://www.bing.com/search?q={team1}+{team2}+sporty+trader+pronostic{str(current_day_number)}+{months[current_month - 1]}+{str(current_year)}+&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ok&sc=8-2&sk=&cvid=D452EBD3F49940C8A8A329E281AD7C4F&ghsh=0&ghacc=0&ghpl=")
        #     print("SportyTrader Link " , linkToGo)
        
        import traceback
        traceback.print_exc()
        return "-999"
        
def Position_Of_A_Team_On_Its_League(S,team,national=False):
    data = teamData()
    if national:
        return 0
    x = pos_league_team(team)
    try:
       S.driver.get(data.all_league_url[x])
    except:
        return -999
    team = team.lower()
    accept_cookie(S)
    for i in range(1,40):
        try:
            element = WebDriverWait(S.driver,2).until(
            EC.presence_of_element_located((By.XPATH, f"/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[{i}]/td[2]")))
            if team == element.text.lower().replace(" ","-"):
                return i
        except:
            return -999

    return -999

def convert_nb_to_100(nb,len_all_nb):
    return int((nb*100)/len_all_nb) + 30

def number_of_team_on_a_league(S,team):
    data = teamData()
    try:

        x = pos_league_team(team)
        try:
            S.driver.get(data.all_league_url[x])
        except:
            return -1
        team = team.lower()
        nb = 0
        for i in range(1,40):
            try:
                element = WebDriverWait(S.driver,2).until(
                EC.presence_of_element_located((By.XPATH, f"/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[{i}]/td[2]")))
                nb=nb+1
            except:
                return nb

        
        return nb
    except:
        return -1
def get_team_of_a_league(S,nb):
    data = teamData()
    S.driver.get(data.all_league_url[nb])
    
    time.sleep(1)
    accept_cookie(S)
    teams = []
    for i in range(1,30):
        try:
            try:
                element = WebDriverWait(S.driver,5).until(
                EC.presence_of_element_located((By.XPATH, f"/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[{str(i)}]/td[2]/a")))
                                                        
            except:
                
                return teams
            teams.append(element.text.lower().replace(" ","-"))
        except:
            return teams
    
    return teams
    
def list_of_team_league(S,url):
    S.driver.get(url)
    
    time.sleep(3)
    accept_cookie(S)

    write_into_file("teamUrl.txt"," "+"\n")
    write_into_file("allteam.txt"," "+"\n")
    print(" ")

    for i in range(1,30):
        try:
            try:
                element = WebDriverWait(S.driver,5).until(
                EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[{str(i)}]/td[2]/a")))
            except:
                return
            print(element.text)
            write_into_file("allteam.txt",element.text.replace(" ","-")+"\n")
            element.click()

            current_url = S.driver.current_url
            #print(current_url)
            write_into_file("teamUrl.txt",current_url+"\n")
            
            S.driver.back()
            time.sleep(3)
        except:
            #import traceback
            #traceback.print_exc()
            return

def add_new_team(S,url):
    S.driver.get(url)
    team_url_data = print_file_info("teamUrl.txt").lower().split("\n")
    all_team_url_data = print_file_info("allteam.txt").lower().split("\n")
    
    for i in range(1,30):
        try:
            try:
                element = WebDriverWait(S.driver,5).until(
                EC.presence_of_element_located((By.XPATH, f"/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[{str(i)}]/td[2]/a")))
            except:

                return
            if (element.text.replace(" ","-").lower() not in all_team_url_data):
                print(element.text)
                write_into_file("allteam.txt",element.text.replace(" ","-")+"\n")
                
                # print(all_team_url_data.index(element.text.replace(" ","-").lower()))
                # time.sleep(3000)
                element.click()

                current_url = S.driver.current_url
                #print(current_url)
                if current_url.lower() not in print_file_info("teamUrl.txt").lower():
                    print(current_url.lower())
                    write_into_file("teamUrl.txt",current_url+"\n")
                
                S.driver.back()
                time.sleep(3)
        except:
            #import traceback
            #traceback.print_exc()
            
            pass

def pos_league_team(team):
    data = teamData()
    for i in range(len(data.allTeam_)):
        _league_team_ = data.allTeam_[i]
        for j in range(len(_league_team_)):
            if team.lower().strip().replace(" ","-") == _league_team_[j].lower().strip().replace(" ","-"):
                return i
    return -1


def get_national_team_list(S):
    acceptButtonXPATH = "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/button[1]"
    S.driver.get("https://www.sofascore.com/football/rankings/fifa")
    element = WebDriverWait(S.driver,5).until(
    EC.presence_of_element_located((By.XPATH, acceptButtonXPATH)))
    element.click()
    national_team_list = []
    try:
        for i in range(4,250):
            teamName = f"/html/body/div[1]/main/div/div/div[1]/div[3]/div[1]/div/div[2]/div[{str(i)}]/div/a/div/div[2]/bdi"
            element = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.XPATH, teamName)))
            print(element.text.replace(" ","-"))
            national_team_list.append(element.text)
            S.driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)
        return national_team_list
    except:
        return national_team_list

def get_url_of_national_team(S,team):
    try:
        S.driver.get(f"https://www.footmercato.net/selection/{team}/calendrier")
        checkTeamExist = "/html/body/div[4]/div[3]/div/div[2]/div[1]/div/h1/div[1]"
        try:
            element = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.XPATH, checkTeamExist)))
            return True , f"https://www.footmercato.net/selection/{team}/calendrier"
        except:
            return False , ""
    except:
            return False , ""            

def get_starting_xi_of_a_team(S,team_url,national=False):
    try:
        if national:
            S.driver.get(team_url.replace("/calendrier","")+"/effectif/"+"#tabMainFormation")
        else:
            S.driver.get(f"{team_url}effectif/#tabMainFormation")
        
        time.sleep(1)
        players = WebDriverWait(S.driver,5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "matchTeamPlayer__name")))
        
        list_of_players = []

        for player in players:
            list_of_players.append(player.text.lower())
    

        return list_of_players
    except:
        return [None]

def get_unavaible_player_of_a_team(S,team_url,national=False):
    try:
        if national:
            S.driver.get(team_url.replace("/calendrier","")+"/effectif")
        else:
            S.driver.get(f"{team_url}effectif")
        
        list_of_players = []
        time.sleep(10)
        element = WebDriverWait(S.driver,1.5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/ul/li[2]/a")))
        element.click()
        time.sleep(5)
        
        if national == False:
            element = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div[3]/div")))
        else:
            element = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div")))

        tablePlayer = element.text
        
        players = WebDriverWait(S.driver,5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "personCardCell__name")))
        
        for player in players:
            if len(player.text) > 1 and player.text in tablePlayer:
                list_of_players.append(player.text.lower())

        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/ul/li[3]/a")))
        element.click()
        time.sleep(5)
        if national == False:
            element = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div[3]/div")))

        else:
            element = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div")))
            
        tablePlayer = element.text
        
        players = WebDriverWait(S.driver,5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "personCardCell__name")))
        
        for player in players:
            if len(player.text) > 1 and player.text in tablePlayer:
                list_of_players.append(player.text.lower())

        list_of_players = list(set(list_of_players))
        return list_of_players    
    except:
        return []

def goal_scored_on_league(S,team_url):
    try:
        S.driver.get(f"{team_url}stats")
        time.sleep(2)
        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[9]/div[2]/div/div[1]/div/span[1]/span[1]")))
        return int(element.text.split("#")[1])
    except:
        return None

def goal_conceded_on_league(S,team_url):
    try:
        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[14]/div[2]/div/div/div/span[1]/span[1]")))
        return int(element.text.split("#")[1])
    except:
        return None

def target_shot_on_league(S,team_url):
    try:
        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[10]/div[2]/div/div[1]/div/span[1]/span[1]")))
        return int(element.text.split("#")[1])
    except:
        return None

def dribble_on_league(S,team_url):
    try:
        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[10]/div[2]/div/div[2]/div/span[1]/span[1]")))
        return int(element.text.split("#")[1])
    except:
        return None

def possession_on_league(S,team_url):
    try:
        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[11]/div[2]/div/div[1]/div/span[1]/span[1]")))
        return int(element.text.split("#")[1])
    except:
        return None

def passing_accuracy_on_league(S,team_url):
    try:
        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[11]/div[2]/div/div[2]/div/span[1]/span[1]")))
        return int(element.text.split("#")[1])
    except:
        return None

def center_accuracy_on_league(S,team_url):
    try:
        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[11]/div[2]/div/div[3]/div/span[1]/span[1]")))
        return int(element.text.split("#")[1])
    except:
        return None

def duel_won_on_league(S,team_url):
    try:
        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[12]/div[2]/div/div[1]/div/span[1]/span[1]")))
        return int(element.text.split("#")[1])
    except:
        return None

def good_tackle_on_league(S,team_url):
    try:
        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[12]/div[2]/div/div[2]/div/span[1]/span[1]")))
        return int(element.text.split("#")[1])
    except:
        return None

def score_of_team_based_on_stat(S,team_url,team,more_stat=False):
    try:
        data = teamData()
        goal_scored = goal_scored_on_league(S,team_url)
        if goal_scored == None:
            return 0
        goal_conced = goal_conceded_on_league(S,team_url)
        if goal_conced == None:
            return 0
        target_shot = target_shot_on_league(S,team_url)
        if target_shot == None:
            return 0
        dribble = dribble_on_league(S,team_url)
        if dribble == None:
            return 0
        possession = possession_on_league(S,team_url)
        if possession == None:
            return 0
        passing_accuracy = passing_accuracy_on_league(S,team_url)
        if passing_accuracy == None:
            return 0
        center_accuracy = center_accuracy_on_league(S,team_url)
        if center_accuracy == None:
            return 0
        good_tackle = good_tackle_on_league(S,team_url)
        if good_tackle == None:
            return 0
        duel_won = duel_won_on_league(S,team_url)
        if duel_won == None:
            return 0
        nb_of_team_on_league = number_of_team_on_a_league(S,team)
        if nb_of_team_on_league == -1:
            return 0
        # print(goal_conced)
        # print(goal_scored)
        # print(target_shot)
        # print(dribble)
        # print(possession)
        # print(passing_accuracy)
        # print(center_accuracy)
        # print(duel_won)
        # print(good_tackle)
        stats_list = [goal_scored * 5,(nb_of_team_on_league - goal_conced) * 5,target_shot*4,dribble*3,possession*3,passing_accuracy * 4,center_accuracy*3,good_tackle * 2,duel_won*2]
        if None in stats_list and more_stat:
            return 0,0
        if None in stats_list and more_stat is False:
            return 0
        #print(stats_list)
        stats_nb = 5 + 5 + 4 + 3 + 3 + 4 + 3 + 2 + 2
        position_based_on_league = int(sum(stats_list)/stats_nb)
        score_based_on_league_and_league_place = int(data.default_score_based_on_the_league[data.pos_league_team] * convert_nb_to_100(data.nb_of_team_on_all_league[data.pos_league_team] - position_based_on_league - 1, data.nb_of_team_on_all_league[data.pos_league_team]))
        # score_based_on_ranking = 10 * 210 + position_based_on_league
        # score_based_on_league_and_league_place = int(score_based_on_ranking * convert_nb_to_100(position_based_on_league , x))
        #print("score_based_on_stat: " , score_based_on_league_and_league_place , team)
        if more_stat:
            return score_based_on_league_and_league_place , position_based_on_league
        else:
            return score_based_on_league_and_league_place
    except:
        return 0

def write_into_file(path, x):
    with open(path, "ab") as f:
        f.write(str(x).encode("utf-8"))

def reset_file(path): 
    try: 
        f = open(path, "w")
        f.write("")    
        f.close            
    except:
        pass

def print_file_info(path):
    f = open(path, 'r',encoding="utf-8")
    content = f.read()
    f.close()
    return(content)