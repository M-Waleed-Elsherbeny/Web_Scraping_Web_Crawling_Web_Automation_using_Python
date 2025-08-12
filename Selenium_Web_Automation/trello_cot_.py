from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import date
import os
import json

BASE_URL = "https://trello.com/"
CHROME_OPTION = webdriver.ChromeOptions()
# CHROME_OPTION.add_argument("--headless")
# CHROME_OPTION.add_argument("--start-maximized")
CHROME_OPTION.add_experimental_option("detach", True) # To Keep Browser Open

DRIVER = webdriver.Chrome(options=CHROME_OPTION)

def login(DRIVER: webdriver.Chrome):
    with open("Selenium_Web_Automation/config.json") as config_file:
        config = json.load(config_file)
    DRIVER.find_element(by=By.XPATH, value='//*[@id="BXP-APP"]/header[1]/div/div[1]/div[2]/a[1]').click()
    time.sleep(2)
    email = DRIVER.find_element(by=By.CSS_SELECTOR, value='input[name="username"]')
    email.clear()
    email.send_keys(config["USERNAME"])
    email.send_keys(Keys.RETURN)
    time.sleep(2)
    password = DRIVER.find_element(by=By.CSS_SELECTOR, value='input[name="password"]')
    password.clear()
    password.send_keys(config["PASSWORD"])
    time.sleep(2)
    login_button = DRIVER.find_element(by=By.ID, value='login-submit')
    login_button.click()
    time.sleep(5)
    # DRIVER.implicitly_wait(5)

def create_new_board(DRIVER: webdriver.Chrome):
    pass
def main():
    try:
        DRIVER.get(BASE_URL)
        DRIVER.maximize_window()
        login(DRIVER=DRIVER)
        create_new_board(DRIVER=DRIVER)
    except Exception as e:
        print(e)
        DRIVER.close()


if __name__ == "__main__":
    main()