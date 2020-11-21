#!/usr/bin/env python
# coding: utf-8

# In[20]:


#-vorher bitte python installiern und dann das programm starten
#-Achtung, ihr dürft nur euren eigenen Content Downloads!!!
#-Dieses Programm darf nicht für Urheberrechts Verletzungen genutzt werden!!
#-------------------------
#-you need python!
#-Attention, you are only allowed to download your own content !!!
#-This program may not be used for copyright infringement !!
#---------------------------------------------------------------------------
import os
import webbrowser
import time
#--------------------------------------------------------------------------
urlbasic = "https://9xbuddy.org/process?url=https%3A%2F%2Fvivo.sx%2F"
url = "https://vivo.sx/51a103acd8"
speak = input("do you speak german(1) oder english(2)")
true = True
#-------------------------
def load(url):
    url = url.strip("https://vivo.sx/")
    gefundenesvideo = ""
    finaleseite = (urlbasic + url)
    print("\n",finaleseite)
    webbrowser.open(finaleseite)
def abfrage():
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
        abfrage()
#-------------------------------------

if True == True:
    abfrage()


# In[ ]:




