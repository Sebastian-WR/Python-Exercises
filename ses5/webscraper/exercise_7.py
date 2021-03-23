import requests 
from bs4 import BeautifulSoup
from markdownify import markdownify

URL = 'https://clbokea.github.io/exam/assignment_2.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser') # bs object that takes the HTML content scraped as input. instantiating bs object also instructing to use the right parser

# open('drdk.html', 'wb').write(page.content)
htmlText = page.text
htmlMD = markdownify(htmlText)
print(htmlMD)
open('BJMD.md', 'w').write(htmlMD)
