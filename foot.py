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
    


def foot_stat(S):
    years = ["2024","2025","2026"]
    S.driver.get("https://www.footmercato.net/club/arsenal/calendrier")

    acceptBtnXpath = "/html/body/div[1]/div/div/div/div/div/div[2]/button[1]"

    element = WebDriverWait(S.driver,15).until(
    EC.presence_of_element_located((By.XPATH, acceptBtnXpath)))

    element.click()
    
    lastResultXpath = "/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/nav/a[2]"
    
    element = WebDriverWait(S.driver,15).until(
    EC.presence_of_element_located((By.XPATH, lastResultXpath)))

    element.click()

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
    team = "Arsenal"
    team = team.lower()
    for i in range(len(lastXmatchSplit)):
        #print(lastXmatchSplit[i])
        if "2024" in lastXmatchSplit[i] or "2025" in lastXmatchSplit[i] or "2026" in lastXmatchSplit[i]:
            
            continue
        else:
            #print("not caca")
            string+= lastXmatchSplit[i].replace(" ","_") + " "
            #print("ok " , lastXmatchSplit[i] , "  " , i , index)
            if index % 4 == 0 and index > 0:
                #print(string)
                index = 0
                listOfResult.append(string.lower())
                string = ""
            
            if len(listOfResult) >= 20:
                break
            index+=1
    #print(lastXmatch)
    
    
    #print(listOfResult)
    #print(len(listOfResult))
    
    win,draw,loose = 0,0,0
    totalOfGame = len(listOfResult)
    for result in listOfResult:
        result = result.split()
        if (team in result[0] and int(result[1]) > int(result[3])) or (team in result[2] and int(result[3]) > int(result[1])):
            print("wiiiiin " , result)
            win+=1
        elif (int(result[1]) == int(result[3])):
            print("draw " , result)
            draw+=1
        else:
            print("loose " , result)
            loose+=1

    print(f"Win {win} {int((win/totalOfGame) * 100)}  %  Draw {win} {int((draw/totalOfGame) * 100)} %  Loose {win} {int((loose/totalOfGame) * 100)} %  Total games {totalOfGame}")
    return
    time.sleep(100)
    return


S = Scraper()
foot_stat(S)