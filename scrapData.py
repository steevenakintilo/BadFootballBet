import feedparser
from random import randint

import requests
from bs4 import BeautifulSoup
from os import system

import pickle
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
import traceback
from discord_webhook import DiscordWebhook

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from os import system
import time
import os.path

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow logs (3 = ERROR)

from teamData import *

class Scraper:
    
    wait_time = 5
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")  # Suppress all logging levels
    driver = webdriver.Chrome(options=options)
    username_xpath = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
    

def accept_cookie(S):
    time.sleep(0.5)
    try:
        acceptBtnXpath = "/html/body/div[1]/div/div/div/div/div/div[2]/button[1]"

        element = WebDriverWait(S.driver,3).until(
        EC.presence_of_element_located((By.XPATH, acceptBtnXpath)))

        element.click()
    except:
        pass    

def is_num(nb):
    try:
        int(nb)
        return True
    except:
        return False
 
def remove_first_two_elem(str):
    words = str.split()
    print("wowowo  " , words)
    if len(words) < 2:
        return str
    unique_words = words[2:]
    return ' '.join(unique_words)

def Get_Last_X_Games_Result(S,team,posTeam):
    
    years = ["2024","2025","2026"]
    all_url = print_file_info("teamUrl.txt").split("\n")
    S.driver.get(all_url[posTeam])

    accept_cookie(S)

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

    for i in range(len(lastXmatchSplit)):
        if "2024" in lastXmatchSplit[i] or "2025" in lastXmatchSplit[i] or "2026" in lastXmatchSplit[i] or "terminé" in lastXmatchSplit[i].lower():
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
                if index == 4 or (change == True and index == 2) and len(string.split()) == 4:
                    listOfResult.append(string.strip().lower())
                    string = ""
                    change = False
                    index = 0
            if len(listOfResult) >= 20:
                break
            #print("index " , index)
            index+=1

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

def list_of_team_league(S,nb):
    if nb == 1:
        S.driver.get("https://www.footmercato.net/club/hac/classement")
    if nb == 2:
        S.driver.get("https://www.footmercato.net/club/liverpool/classement")
    if nb == 3:
        S.driver.get("https://www.footmercato.net/club/fc-barcelone/classement")
    if nb == 4:
        S.driver.get("https://www.footmercato.net/club/bayer-04-leverkusen/classement")
    if nb == 5:
        S.driver.get("https://www.footmercato.net/club/inter/classement")
    if nb == 6:
        S.driver.get("https://www.footmercato.net/club/sporting-clube-de-portugal/classement")
    if nb == 7:
        S.driver.get("https://www.footmercato.net/club/feyenoord-rotterdam/classement")
    if nb == 8:
        S.driver.get("https://www.footmercato.net/club/galatasaray-spor-kulubu/classement")
    if nb == 9:
        S.driver.get("https://www.footmercato.net/club/club-brugge-kv/classement")
    if nb == 10:
        S.driver.get("https://www.footmercato.net/club/bsc-young-boys/classement")


    accept_cookie(S)

    #time.sleep(101010)

    for i in range(1,30):
        try:
            element = WebDriverWait(S.driver,2).until(
            EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[{str(i)}]/td[2]/a")))
            print(element.text)
            element.click()

            current_url = S.driver.current_url
            print(current_url)
            write_into_file("teamUrl.txt",current_url+"\n")
            S.driver.back()
            time.sleep(3)
        except:
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
