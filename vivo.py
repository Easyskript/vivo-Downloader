

import os
import webbrowser

#----------------------------
urlbasic = "https://9xbuddy.org/process?url=https%3A%2F%2Fvivo.sx%2F"
url = "https://vivo.sx/51a103acd8"
url = input("vivo link zum Download eintippen:  ")
url = url.strip("https://vivo.sx/")

gefundenesvideo = ""
finaleseite = (urlbasic + url)
print(finaleseite)
webbrowser.open(finaleseite)