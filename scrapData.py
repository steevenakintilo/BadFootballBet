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
    #print("caca " , len(sprint_pkl_info()),print_pkl_info())
    driver = webdriver.Chrome(options=options)
    username_xpath = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
    

def accept_cookie(S):
    time.sleep(0.5)
    try:
        try:
            ck = print_pkl_info()
        except:
            ck = ""
        if len(str(ck)) > 20:
            cookies = pickle.load(open(f"cookies{0}.pkl","rb"))
            for cookie in cookies:
                S.driver.add_cookie(cookie)

        else:
            acceptBtnXpath = "/html/body/div[1]/div/div/div/div/div/div[2]/button[1]"

            element = WebDriverWait(S.driver,3).until(
            EC.presence_of_element_located((By.XPATH, acceptBtnXpath)))

            element.click()
            pickle.dump(S.driver.get_cookies(), open(f"cookies{0}.pkl", "wb"))
    except:
        import traceback
        traceback.print_exc()    
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
        time.sleep(3)
        return all_url[posTeam]
    except:
        return("")
def Get_Last_X_Games_Result(S,team,posTeam,nbOfGameToAnalyze=20):
    
    years = ["2024","2025","2026"]
    all_url = print_file_info("teamUrl.txt").split("\n")
    S.driver.get(all_url[posTeam])

    #accept_cookie(S)

    time.sleep(5)

    S.driver.get(f"{all_url[posTeam]}calendrier/#tabPlayed")
    time.sleep(5)
    lastResultXpath = "/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/nav/a[2]"
    
    calendarXpath = "/html/body/div[3]/div[4]/div/div/nav/ul/li[4]/a"

    time.sleep(1)
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
        print(f"Sorry but {team} has played 0 match this season can't compare or get that stat of it")
        S.driver.close()
        quit()
    return listOfResult
    



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
            write_into_file("allteam.txt",element.text+"\n")
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
    f = open(path, "w")
    f.write("")    
    f.close            

def print_file_info(path):
    f = open(path, 'r',encoding="utf-8")
    content = f.read()
    f.close()
    return(content)
