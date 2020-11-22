
#put the  chromedriver exe in the same folder !!!!!!!
#see your chrome version: https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have
#Download your versions chromedriver here: https://chromedriver.chromium.org/downloads
#-you need python!
#-Attention, you are only allowed to download your own content !!!
#-This program may not be used for copyright infringement !!
#---------------------------------------------------------------------------
!pip install selenium
import os
import webbrowser
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#--------------------------------------------------------------------------
urlbasic = "https://9xbuddy.org/process?url=https%3A%2F%2Fvivo.sx%2F"
url = "https://vivo.sx/51a103acd8"
speak = input("do you speak german(1) oder english(2)")
true = True
#-------------------------
def load(url):
    url = url.strip("https://vivo.sx/")
    finaleseite = (urlbasic + url)
    webbrowser.open(finaleseite)
    PATH = "./chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(finaleseite)
    time.sleep(2)
    link = driver.find_element_by_xpath('(//SPAN)[36]')
    link.click()
#--------------------------------------
def lan():
    if speak == "1":
        print("\n, Eiso sprichst du Deutsch finde ich gut ")
        url = input("hier kommt der Vivo Link rein:  ")
        load(url)
    elif speak == "2":
        print("\n nice you speak english Nice ")
        url = input("Enter the Vivo URL pls:  ")
        load(url)
    else:
        time.sleep(1)
        lan()
#-------------------------------------

if True == True:
    lan()
