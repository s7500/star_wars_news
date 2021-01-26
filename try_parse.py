import pprint

import requests
from bs4 import BeautifulSoup

"""
parser for news feed
It would be cool to finish off the Star Wars project
"""
url = 'https://ria.ru/lenta/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
content = soup.find_all('div', {'class': 'list-item'})

with open('news.json', 'w') as output_file:
    for item in content:
        news = item.find_all('a')[-1]
        output_file.write(news.contents[0] + '\n')
