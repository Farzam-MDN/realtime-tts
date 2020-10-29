
import os
import requests
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import keyboard
from selenium.webdriver.common.keys import Keys
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from datetime import datetime


global chrome_path
#chrome_path  = r"C:\Users\madan\anaconda3\Lib\chromedriver_win32\chromedriver.exe"
chrome_path = 'chromedriver/chromedriver.exe'

global  driver
global status
status = True

    ##headless

#chrome_options = Options()
##chrome_options.add_argument("--headless")
##chrome_options.add_argument("--start-maximized")


#chrome_options.add_argument("user-data-dir=C:\\Users\\madan\\AppData\\Local\\Google\\Chrome\\User Data")
##chrome_options.add_argument("user-data-dir=C:\\Users\\madan\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
##options.add_argument('--profile-directory=Profile 2')
##driver = webdriver.Chrome(chrome_path,options=chrome_options)

#chrome profie C:\Users\madan\AppData\Local\Google\Chrome\User Data\Default


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

print('Welcome to the realtime-tts application. You can use this application to directly turn your typed words into speech! ')
#driver = webdriver.Chrome(chrome_path,options=chrome_options)
driver = webdriver.Chrome(chrome_path,options=options)
driver.set_window_position(-10000,0)
driver.get('https://translate.google.com')

time.sleep(2)

while status == True:
    print("Type your text and press enter:")

    usertext = input("")
    if usertext != '':
        driver.find_element_by_xpath("""//*[@id="source"]""").clear()
        driver.find_element_by_xpath("""//*[@id="source"]""").send_keys(usertext)
        time.sleep(.5)
        driver.find_element_by_xpath("""/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[4]/div[5]/div""").click()

#texbox:
# //*[@id="source"]

#speech button
# //*[@id="gt-speech"]/span




