# pip install beautifulsoup4f
# pip install requests

from bs4 import BeautifulSoup
import requests

url = "https://www.thejakartapost.com/news/2020/03/27/mayapada-group-tahir-foundation-donate-rp-52b-to-fight-covid-19.html"

req = requests.get(url)

if req.status_code == 200:
    response = req.text
    
    soup = BeautifulSoup(response, 'html.parser')

    headings = soup.find_all('h1')

    '''
    for h in headings:
        print(h)
    '''

    paragraphs = soup.select('div.detailNews p')

    # print(soup.title.text)

    print(soup.select('h1.title-large')[0].text)

    for p in paragraphs:
        print(p.text + '\n')

    
