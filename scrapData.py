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

from teamData import *

class Scraper:
    
    wait_time = 5
    #headless = data["headless"]
    options = webdriver.ChromeOptions()
    
    
    # #proxy_server_url = "185.199.229.156"
    # #options.add_argument(f'--proxy-server={proxy_server_url}')
    #options.add_argument('headless')
    options.add_argument("--log-level=3")  # Suppress all logging levels
    
    # driver = webdriver.Chrome(options=options)  # to open the chromedriver    
    # FIREFOX

    #options = webdriver.FirefoxOptions()
    #options.headless = False

    driver = webdriver.Chrome(options=options)
    
    # CACA
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

def Get_Last_X_Games_Result(S,team,posTeam):
    
    years = ["2024","2025","2026"]
    all_url = print_file_info("teamUrl.txt").split("\n")
    S.driver.get(all_url[posTeam])

    accept_cookie(S)

    lastResultXpath = "/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/nav/a[2]"
    
    calendarXpath = "/html/body/div[3]/div[4]/div/div/nav/ul/li[4]/a"

    try:
        element = WebDriverWait(S.driver,3).until(
        EC.presence_of_element_located((By.XPATH, calendarXpath)))

        element.click()

    except:
        pass

    element = WebDriverWait(S.driver,3).until(
    EC.presence_of_element_located((By.XPATH, lastResultXpath)))

    element.click()

    time.sleep(1)
    tabResultXpath = "/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/div"

    element = WebDriverWait(S.driver,3).until(
    EC.presence_of_element_located((By.XPATH, tabResultXpath)))

    listOfResult = []
    lastXmatch = element.text
    lastXmatchSplit = lastXmatch.split("\n")
    index = 1
    string = ""
    first = True
    team = team.lower()
    for i in range(len(lastXmatchSplit)):
        #print(lastXmatchSplit[i])
        if "2024" in lastXmatchSplit[i] or "2025" in lastXmatchSplit[i] or "2026" in lastXmatchSplit[i] or "terminé" in lastXmatchSplit[i].lower():
            continue
        else:
            #print("not caca")
            string+= lastXmatchSplit[i].replace(" ","-") + " "
            #print("ok " , lastXmatchSplit[i] , "  " , i , index)
            if index % 4 == 0 and index > 0:
                #print(string)
                index = 0
                listOfResult.append(string.lower())
                string = ""
            
            if len(listOfResult) >= 20:
                break
            index+=1

    return listOfResult




def Position_Of_A_Team_On_Its_League(S,team):
    data = teamData()
    x = pos_league_team(team)
    S.driver.get(data.all_league_url[x])
    team = team.lower()
    accept_cookie(S)
    for i in range(1,40):
        try:
            element = WebDriverWait(S.driver,2).until(
            EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[{str(i)}]/td[2]/a/span")))
            if team == element.text.lower().replace(" ","-"):
                return i
            #time.sleep(3)
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
