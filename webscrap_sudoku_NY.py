import webbrowser
import requests
from bs4 import BeautifulSoup
import json
import numpy as np
from greedyBacktrack import greedyBacktrack_visualiser
import time
from sys import platform
import os
import pyautogui as pg

difficulty = "medium"
url = "https://www.nytimes.com/puzzles/sudoku/" + difficulty

if platform == "linux" or platform == "linux2":
    browser_path = '/usr/bin/microsoft-edge %s --incognito'
    webbrowser.get(browser_path).open(url)

elif platform == "darwin":
    browser_path = 'open -a /Applications/Google\ Chrome.app %s --incognito'     
    os.system("open -na \"Google Chrome\" --args --incognito \"{}\"".format(url)) 

elif platform == "win32":
    browser_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe --incognito %s'
    webbrowser.get(browser_path).open_new(url)


page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser") 
table = soup.find_all("div", {"class":"pz-game-screen"})[0]
script = table.find_all("script", {"type":"text/javascript"})
text = script[0].get_text().split("=")[1]
Dict = json.loads(text)
grid = np.array( Dict[difficulty]["puzzle_data"]["puzzle"] ).reshape(9,9).tolist()


time.sleep(3) 
pg.press('left', presses = 9) 
greedyBacktrack_visualiser(grid) 