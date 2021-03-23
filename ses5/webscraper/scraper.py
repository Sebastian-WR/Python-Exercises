import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

URL = 'https://www.jobindex.dk/jobsoegning/storkoebenhavn?q=python'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser') # bs object that takes the HTML content scraped as input. instantiating bs object also instructing to use the right parser

results = soup.find(id='result_list_box')
# print(results.prettify())
job_elems = results.find_all(class_='jobsearch-result')
""" for job_elem in job_elems:
    print(job_elem, end='\n'*2) """

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('b').text # finder det første <b> tag i div og printer det i text format som er job titel
    company_elem = job_elem.find('p').find('b').text # finder den første <p> og derefter den første <b> deri som er firma printer i text format
    location_elem = job_elem.find('p').text.split() # finder den første <p> og printer til text, splitter den op så jeg kan få lokation kun som sidste i listen
    print(title_elem.strip()) ## her printer jeg dem alle med strip for at fjerne whitespace omkring dem og den sidste tager -1 i hver liste som er sidste index == lokationen
    print(company_elem.strip())
    print(location_elem[-1].strip())
    print()
