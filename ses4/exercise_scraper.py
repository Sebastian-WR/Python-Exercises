import requests
import webbrowser
import os
import codecs


print("Enter the URL you want to download the HTML for: ")
consInput = input()
url = consInput
r = requests.get(url, allow_redirects=True)
open('drdk.html', 'wb').write(r.content)
webbrowser.open_new('file://' + os.path.abspath('exercise_scraper.py'))
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open('file://' + os.path.abspath('exercise_scraper.py'))
codecs.open("drdk.html", "r", "utf-8")
webbrowser.open('https://www.dr.dk/nyheder')
