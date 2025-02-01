from random import randint

import requests
from os import system

import pickle
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from os import system
import time
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

def accept_cookie(S):
    if print_file_info("ckk.txt") == "1":
        return
    try:
        try:
            ck = print_pkl_info()
        except:
            ck = ""
        if len(str(ck)) > 20:
            cookies = pickle.load(open(f"cookies{0}.pkl","rb"))
            for cookie in cookies:
                S.driver.add_cookie(cookie)
            write_into_file("ckk.txt",1)
            
        else:
            reset_file("ckk.txt")
            acceptBtnXpath = "/html/body/div[1]/div/div/div/div/div/div[2]/button[1]"

            element = WebDriverWait(S.driver,3).until(
            EC.presence_of_element_located((By.XPATH, acceptBtnXpath)))

            element.click()
            pickle.dump(S.driver.get_cookies(), open(f"cookies{0}.pkl", "wb"))
            write_into_file("ckk.txt",1)

    except:
        #import traceback
        #traceback.print_exc()    
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
    accept_cookie(S)
    allTeam = print_file_info("allteam.txt").lower().split("\n")

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
    #S.driver.get(f"https://www.footmercato.net/live/")

    time.sleep(3)
    page_text = S.driver.find_element(By.TAG_NAME, "body").text
    skipMatches = page_text.split("Amicaux Club")
    list_of_matches = []
    striiing = ""
    error = 0
    skip = False
    for j in range(3,60):
        for i in range(1,60):
            try:
                test = f"/html/body/div[3]/div[3]/div/div[1]/div[{j}]/div[2]/div[{i}]/div/a/span[1]"
                element = WebDriverWait(S.driver,3).until(
                EC.presence_of_element_located((By.XPATH, test)))
                matches = element.text.replace(" ","-").split("\n")
                if element.text in skipMatches[1]:
                    skip = True
                if matches[0].lower() in allTeam and matches[1].lower() in allTeam and skip != True:
                    list_of_matches.append(matches[0] + "#####" + matches[1])
                error = 0
            except:
                error+=1
                if error > 5:
                    return list_of_matches
                break
    
    return list_of_matches

def Get_Last_X_Games_Result(S,team,posTeam,nbOfGameToAnalyze=20):
    
    years = ["2024","2025","2026"]
    all_url = print_file_info("teamUrl.txt").split("\n")
    #S.driver.get(all_url[posTeam])

    #accept_cookie(S)

    #time.sleep(5)

    S.driver.get(f"{all_url[posTeam]}calendrier/#tabPlayed")
    lastResultXpath = "/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/nav/a[2]"
    
    calendarXpath = "/html/body/div[3]/div[4]/div/div/nav/ul/li[4]/a"

    tabResultXpath = "/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/div"

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
    #print(lastXmatchSplit)
    
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


def has_Team_Played_since_september(S,team,posTeam):
    
    try:
        all_url = print_file_info("teamUrl.txt").split("\n")
        S.driver.get(f"{all_url[posTeam]}calendrier/#tabPlayed")
        tabResultXpath = "/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div"

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

def get_odds(S,team1,team2,result,FirstResultOdd=False):
    now = datetime.now()
    months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    current_day_number = now.day
    current_year = now.year  # Year (e.g., 2025)
    current_month = now.month

    try:
        team1=team1.lower()
        team2=team2.lower()
        if FirstResultOdd == False:
            S.driver.get(f"https://www.bing.com/search?q={team1}+{team2}+sporty+trader+pronostic&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ok&sc=8-2&sk=&cvid=D452EBD3F49940C8A8A329E281AD7C4F&ghsh=0&ghacc=0&ghpl=")
        else:
            S.driver.get(f"https://www.bing.com/search?q={team1}+{team2}+sporty+trader+pronostic{str(current_day_number)}+{months[current_month - 1]}+{str(current_year)}+&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ok&sc=8-2&sk=&cvid=D452EBD3F49940C8A8A329E281AD7C4F&ghsh=0&ghacc=0&ghpl=")
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
                if "sportytrader.com" in link:
                    linkToGo = link
                    break

        S.driver.get(linkToGo)
        S.driver.execute_script("document.body.style.zoom='30%'")
        time.sleep(3)
        tableCote2 = "/html/body/div[1]/div[3]/div[4]/section/main/div[1]/section[1]"
        tc = "/html/body/div[1]/div[3]/div[4]/section/main/section[2]/div[1]/div/table/tbody"
        
        t1Name = ""
        t2Name = ""
        team1P = "/html/body/div[1]/div[3]/div[4]/section/main/div[2]/div[1]/div[2]/div[1]"
        team2P = "/html/body/div[1]/div[3]/div[4]/section/main/div[2]/div[1]/div[2]/div[3]"
        
        element = WebDriverWait(S.driver,25).until(
        EC.presence_of_element_located((By.XPATH, team1P)))
        t1Name = element.text.lower()

        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, team2P)))
        t2Name = element.text.lower()
        reverse=False

        if t2Name in team1 or team1 in t2Name or team1 == t2Name or check_split(team1,t2Name) == True:
            reverse = True
            #print("reeeveeeerseeeeee " , team1 , team2)
          
        if t1Name in team2 or team2 in t1Name or team2 == t1Name or check_split(team2,t1Name) == True:
            reverse = True
            #print("reeeveeeerseeeeee " , team1 , team2)
        
        if team1 in team2 or team2 in team1:
            #print("both team have a commun name " , team1,team2)
            reverse = False
        
        try:
            fullTableCote = WebDriverWait(S.driver,5).until(
            EC.presence_of_element_located((By.XPATH, tc)))
        except:
            try:
                fullTableCote = WebDriverWait(S.driver,5).until(
                EC.presence_of_element_located((By.XPATH, tableCote2)))
            except:
                # import traceback
                # traceback.print_exc()
                # print("flop 1")
                return "-999"
        odds = fullTableCote.text.split("\n")
        #print(f"t1 {t1Name} t2 {t2Name} {odds}")
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
        # import traceback
        # traceback.print_exc()
        # print("flop 2")
        return "-999"
        
def Position_Of_A_Team_On_Its_League(S,team):
    data = teamData()
    x = pos_league_team(team)
    try:
       S.driver.get(data.all_league_url[x])
    except:
       time.sleep(120)
       S.driver.get(data.all_league_url[x])
    team = team.lower()
    accept_cookie(S)
    for i in range(1,40):
        try:
            element = WebDriverWait(S.driver,2).until(
            EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[{str(i)}]/td[2]/a/span")))
            if team == element.text.lower().replace(" ","-"):
                return i
        except:
            return -999

    return -999
    

def checkTeamNameIsRight(S,teamName):
    try:
        S.driver.get(f"https://www.footmercato.net/club/{teamName}/calendrier")

        acceptBtnXpath = "/html/body/div[1]/div/div/div/div/div/div[2]/button[1]"

        element = WebDriverWait(S.driver,0.01).until(
        EC.presence_of_element_located((By.XPATH, acceptBtnXpath)))

        return True
    except:
        print(teamName)
        return False


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
                EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[{str(i)}]/td[2]/a")))
            except:
                return teams
            teams.append(element.text.lower().replace(" ","-"))
        except:
            #import traceback
            #traceback.print_exc()
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


def pos_league_team(team):
    data = teamData()
    for i in range(len(data.allTeam_)):
        _league_team_ = data.allTeam_[i]
        for j in range(len(_league_team_)):
            if team.lower().strip().replace(" ","-") == _league_team_[j].lower().strip().replace(" ","-"):
                return i
    return -1

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