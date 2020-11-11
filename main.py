import requests
import time
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pprint

url = "https://energycentral.com/news"

chrome_options = Options()
chrome_options.add_argument("--headless")  # Opens the browser up in background

with Chrome(options=chrome_options) as browser:
    browser.get(url)
    html = browser.page_source

page_soup = BeautifulSoup(html, 'html.parser')

links_list = []
for i in page_soup.find_all('span', {'class': 'article-title'}):
    link = i.find('a', href=True)
    if link is None:
        continue
    links_list.append(link['href'])

title_list = []
for i in page_soup.find_all('span', {'class': 'article-title'}):
    title = i.find('span')
    if title is None:
        continue
    title_list.append(i.getText())

title_link_dict = dict(zip(title_list, links_list))

pprint.pprint(title_link_dict)
