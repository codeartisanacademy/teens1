from bs4 import BeautifulSoup
import requests

url = 'https://www.thejakartapost.com'

# go to the website
req = requests.get(url)

if req.status_code == 200:
    response = req.text
    soup = BeautifulSoup(response, 'html.parser')

    latests = soup.select('div.listNews h2.titleNews')

    for l in latests:
        print(l.text)