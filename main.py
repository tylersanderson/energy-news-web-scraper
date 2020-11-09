import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pprint


url = "https://energycentral.com/news"
browser = webdriver.Chrome()
browser.get(url)
# time.sleep(30)
html = browser.page_source

soup = BeautifulSoup(html, 'lxml')
#soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.article-title-link')
title = soup.select('.article-title')
main = soup.select('.content')
#links2 = soup2.select('.storylink')
#subtext2 = soup2.select('.subtext')

mega_links = links  # + links2
# mega_subtext = subtext  # + subtext2


#pprint.pprint(create_custom_hn(links, title))
pprint.pprint(soup)
# print(soup)
