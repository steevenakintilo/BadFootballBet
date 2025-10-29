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

def write_into_file(path, x):
    with open(path, "ab") as f:
        f.write(str(x).encode("utf-8"))

class Scrapper:
    def __init__(self, ):
        self.wait_time = 5
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--log-level=1')
        self.options.add_argument('--log-level=3')  # Suppress all logging levels
        # self.options.add_argument('--blink-settings=imagesEnabled=false')

        # Set headless mode based on the parameter
        
        self.options.add_argument('--disable-gpu')  # Disable GPU (helpful in headless mode)
        self.options.add_argument('--disable-dev-shm-usage')  # Prevent shared memory issues

        # Initialize the WebDriver
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.set_page_load_timeout(15)



def get_oods_of_a_match(team1,team2,result,prono=False):
    try:
        S = Scrapper()
        team1 = team1.replace("-" ," ")
        team2 = team2.replace("-" ," ")
        
        team_to_rename = {"psg":"Paris SG",
        "calcio padova":"padoue",
        "husa":"Hassania Agadir",
        "wydad":"Wydad Casablanca",
        "raja":"Raja Casablanca"}

        try:
            team1 = team_to_rename[team1].lower()
        except:
            pass
        
        try:
            team2 = team_to_rename[team2].lower()
        except:
            pass
        
        try:
            S.driver.get("https://www.winamax.fr/paris-sportifs/")
        except:
            S.driver.refresh()
            time.sleep(5)
        close_btn_xpath = "/html/body/div[3]/div/div/section/div/div[2]/div[2]/div[2]/div/div[1]/div[2]"
        element = WebDriverWait(S.driver,10).until(
        EC.presence_of_element_located((By.XPATH, close_btn_xpath)))
        element.click()
        search_bar_xpath="/html/body/div[3]/div/div/section/div/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div/div[2]/input"
        element = WebDriverWait(S.driver,3).until(
        EC.presence_of_element_located((By.XPATH, search_bar_xpath)))
        element.click()
        element.send_keys(team1 + " " + team2)
        time.sleep(3)
        result_xpath = "/html/body/div[3]/div/div/section/div/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div/div[1]/div[2]/a"
        element = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, result_xpath)))
        element.click()
        left_result_xpath = "/html/body/div[3]/div/div/section/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/div[4]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]"
        middle_result_xpath = "/html/body/div[3]/div/div/section/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/div[4]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]"
        right_result_xpath = "/html/body/div[3]/div/div/section/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/div[4]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[3]/div[2]/div[1]"
        

        
        left_result = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, left_result_xpath))).text
        
        middle_result = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, middle_result_xpath))).text
        
        right_result = WebDriverWait(S.driver,5).until(
        EC.presence_of_element_located((By.XPATH, right_result_xpath))).text
        
        if len(left_result.split("\n")) > 2:
            left_result = [left_result.split("\n")[1],left_result.split("\n")[2]]
        else:
            left_result = left_result.split("\n")
        if len(middle_result.split("\n")) > 2:
            middle_result = [middle_result.split("\n")[1],middle_result.split("\n")[2]]
        else:
            middle_result = middle_result.split("\n")
        if len(right_result.split("\n")) > 2:
            right_result = [right_result.split("\n")[1],right_result.split("\n")[2]]
        else:
            right_result = right_result.split("\n")
        
        if prono is False:
            if result == "draw":
                S.driver.close()
                return middle_result[1]
            
            if result.lower() in str(left_result).lower().replace("-"," "):
                S.driver.close()
                return left_result[1]
            
            if result.lower() in str(right_result).lower().replace("-"," "):
                S.driver.close()
                return right_result[1]    
            S.driver.close()
            return f"Fail {team1} VS {team2}"
        
        data = [left_result,middle_result,right_result]
        sorted_data = sorted(data, key=lambda x: float(x[1].replace(',', '.')))
        S.driver.close()
        return sorted_data[0][0]    
    except:
        S.driver.close()
        write_into_file("rename_team_for_odds.txt",f"Fail {team1} VS {team2}"+"\n")
        return f"Fail {team1} VS {team2}"