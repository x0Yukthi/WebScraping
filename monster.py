'''A web scraper to find the perfect job'''
import requests
from bs4 import BeautifulSoup

url = "https://www.monster.com/jobs/search/?q=Software-Developer&where=India"
wpages = requests.get(url)
bs = BeautifulSoup(wpages.content, 'html.parser')
results = bs.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    t_elem = job_elem.find('h2', class_='title')
    c_elem = job_elem.find('div', class_='company')
    l_elem = job_elem.find('div', class_='location')
    if None in (t_elem, c_elem, l_elem):
        continue
    print(t_elem.text)
    print(c_elem.text)
    print(l_elem.text)
    print()
p_jobs = results.find_all('h2', string='Python Developer')
p_jobs = results.find_all('h2',string=lambda text: 'python' in text.lower())
for p_job in p_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")
