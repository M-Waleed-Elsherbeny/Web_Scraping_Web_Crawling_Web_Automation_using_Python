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

def navigateToBoard(DRIVER: webdriver.Chrome):
    time.sleep(5)
    DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);") # to scroll to the bottom of the page.
    time.sleep(2)
    DRIVER.find_element(By.XPATH, '//span[@class="GOPk_J9hMP7py5"]').click()

def addTask(DRIVER: webdriver.Chrome):
    time.sleep(5)
    DRIVER.find_element(By.CSS_SELECTOR, 'button[aria-label="Add a card in Today"]').click()
    time.sleep(2)
    addCard = DRIVER.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Enter a title or paste a link"]')
    addCard.clear()
    addCard.send_keys("Add Task From Python Script")
    addCard.send_keys(Keys.ENTER)
    DRIVER.find_element(By.CSS_SELECTOR, 'button[aria-label="Cancel new card"]').click()
    time.sleep(2)

def takeScreenShot(DRIVER: webdriver.Chrome):
    fileName = date.today().strftime("%d-%m-%Y")
    DRIVER.save_screenshot(f"Selenium_Web_Automation/Add_Task_Image/{fileName}.png")
    
def main():
    try:
        DRIVER.get(BASE_URL)
        DRIVER.maximize_window()
        login(DRIVER=DRIVER)
        navigateToBoard(DRIVER=DRIVER)
        addTask(DRIVER=DRIVER)
        takeScreenShot(DRIVER=DRIVER)
    except Exception as e:
        print(e)
        DRIVER.close()
    finally:
        DRIVER.close()


if __name__ == "__main__":
    main()