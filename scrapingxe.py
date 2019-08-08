import requests
from bs4 import BeautifulSoup

url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=IDR'

web = requests.get(url)

response = web.text

soup = BeautifulSoup(response, 'html.parser')

print(soup.head.title.get_text())

print(soup)
print(amount)