from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import date
import os

BASE_URL = "https://trello.com/"
CHROME_OPTION = webdriver.ChromeOptions()
# CHROME_OPTION.add_argument("--headless")
CHROME_OPTION.add_argument("--start-maximized")
CHROME_OPTION.add_experimental_option("detach", True) # To Keep Browser Open
# CHROME_SERVICE = webdriver.ChromeService(os.path.join(os.getcwd(), "Selenium_Web_Automation/chromedriver.exe"))

DRIVER = webdriver.Chrome(options=CHROME_OPTION)

def main():
    try:
        DRIVER.get(BASE_URL)
    except Exception as e:
        print(e)
        DRIVER.close()


if __name__ == "__main__":
    main()