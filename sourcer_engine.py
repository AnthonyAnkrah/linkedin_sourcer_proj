import time
import csv
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions

def init_driver(extensions:list):
    # Init Options
    options = ChromeOptions()
    for ext in extensions:
        # options.add_extension(ext)
        options.add_argument(
            "--load-extension=" + ext)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    return driver

def visit_url(driver, url, class_xpath_verifier):
    time.sleep(1)
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, class_xpath_verifier)))
    except:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, class_xpath_verifier)))
    return driver

def sign_in(driver, auth_dets:dict):
    driver.get("https://www.linkedin.com/")
    user = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='session_key']")))
    user.send_keys(auth_dets['user'])
    user = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='session_password']")))
    user.send_keys(auth_dets['pass'])
    signin_btn = driver.find_element_by_xpath("//button[@class='sign-in-form__submit-button']")
    signin_btn.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger']")))
    return driver

def show_extension(images: list):
    time.sleep(1)
    all_extn_icon = pyautogui.locateOnScreen(images[0])
    all_extn_cdnt = pyautogui.center(all_extn_icon)
    extn_x, extn_y = all_extn_cdnt
    pyautogui.click(x=extn_x, y=extn_y, clicks=1, interval=0.0, button="left")
    time.sleep(1)
    # Look for pin icon ansd click
    pin_me_icon = pyautogui.locateOnScreen(images[1])
    pin_me = pyautogui.center(pin_me_icon)
    pin_x, pin_y = pin_me
    pyautogui.click(x=pin_x, y=pin_y, clicks=1, interval=0.0, button="left")
    time.sleep(1)
    pyautogui.click(x=966,y=1,button='left')

def click_extension(image):
    time.sleep(1)
    extn_icon = pyautogui.locateOnScreen(image)
    extn_cdnt = pyautogui.center(extn_icon)
    extn_x, extn_y = extn_cdnt
    # click on extension 
    pyautogui.click(x=extn_x,y=extn_y,clicks=1,interval=0.0,button="left")
    time.sleep(1)
