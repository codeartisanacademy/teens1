from bs4 import BeautifulSoup
import requests

url = 'https://nasional.kompas.com'

# request the page. Like opening a web page
kompas_request = requests.get(url)

# accept the response
kompas_response = kompas_request.text

soup = BeautifulSoup(kompas_response, 'html.parser')

title_content_list = soup.select('.title__content')
terpopuler_text = None
for t in title_content_list:
    if t.get_text() == 'Terpopuler':
        terpopuler_text = t

parent_terpopuler = terpopuler_text.find_parent()

terpopuler_container = parent_terpopuler.find_next_sibling()

terpopuler_text = terpopuler_container.find_all('h4')

for t in terpopuler_text:
    print(t.get_text())

'''
soup = BeautifulSoup(kompas_response, 'html.parser')

title_content_list = soup.select('.title__content')
terpopuler = None

for title in title_content_list:
    if title.get_text() == 'Terpopuler':
        terpopuler = title

parent = terpopuler.find_parent()

terpopuler_list = parent.find_next_sibling()

terpopuler_list_text = terpopuler_list.find_all('a')

for t in terpopuler_list_text:
    print(t.get_text())

'''






