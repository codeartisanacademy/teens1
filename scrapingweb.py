import requests
from bs4 import BeautifulSoup

url = 'https://www.thejakartapost.com/news'

web = requests.get(url)

response = web.text

#print(response)

soup = BeautifulSoup(response, 'html.parser')

news_contributor = soup.find(id='newsContributor')

list_news = news_contributor.select('.titleNews')

for n in list_news:
    print(n.get_text())