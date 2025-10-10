# Importing my chatgpt scrapper code to avoid recoding the same stuff for cover letter
# pylint: disable=all

import time
import undetected_chromedriver as uc 
import traceback

from global_variable import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

uc.Chrome.__del__ = lambda self: None

class GptScraper:
    
    def __init__(self):
        self.options = uc.ChromeOptions()
        self.options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        self.options.add_argument('headless')
        self.options.add_argument(f'--user-agent={ua}')
        self.driver = uc.Chrome(options=self.options)
        self.answer_list:list[str] = []
        self.query:str = ""

    def maker(self,questions):
        try:
            question = questions[0].replace("\n"," ")
            self.query = question
            self.scrapping()
        finally:
            try:
                self.driver.quit()
            except:
                pass
        return self.answer_list[0]

    
    def scrapping(self):
        for _ in range(3):
            try:
                self.driver.get(mainpage)
                time.sleep(5)

                login_button_datatestid
                try:
                    element = WebDriverWait(self.driver,wait_time_gpt).until(
                    EC.presence_of_element_located((By.XPATH, By.CSS_SELECTOR, f'[data-testid={login_button_datatestid}]')))
                except Exception as e:
                    self.driver.refresh()
                    time.sleep(5)
                    self.driver.get(mainpage)
                    time.sleep(5)
    
                    pass
                try:
                    accept_cookies_xpath_element = WebDriverWait(self.driver,wait_time_gpt).until(
                    EC.presence_of_element_located((By.XPATH, accept_cookies_gpt_xpath)))
                    accept_cookies_xpath_element.click()
                    time.sleep(5)
                except:
                    pass

                
                try:
                    element = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, stay_logout_xpath)))
                    time.sleep(2)
                    element.click()
                    time.sleep(2)
                except:
                    pass

                time.sleep(1)
                self.driver.refresh()
                time.sleep(2.5)
                time.sleep(2.5)

                actions = ActionChains(self.driver)
                actions.send_keys(self.query).perform()
                actions.send_keys(Keys.RETURN).perform()
                
                time.sleep(wait_time_gpt2)
                
                for i in range(25):
                    get_url = self.driver.current_url
                    if "https://chat.openai.com/auth/login" in get_url:
                        return ""
                    try:
                        element = self.driver.find_element(By.CSS_SELECTOR, f'[data-testid={stop_btn_datestid}]')
                        time.sleep(12)
                    except Exception as e:
                        pass
                try:
                    element = WebDriverWait(self.driver, wait_time_gpt).until(
                    EC.presence_of_element_located((By.XPATH, answer_xpath)))
                    answer = element.text
                    self.answer_list.append(answer.replace("ChatGPT",""))
                except:
                    pass
                    
                return ""
            except:
                traceback.print_exc()
            return ""
