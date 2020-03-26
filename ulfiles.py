import requests
from bs4 import BeautifulSoup

url = 'https://fairwayfiles.com/find_user.php?uname=underline&'

web = requests.get(url)

response = web.text

soup = BeautifulSoup(response, 'html.parser')

table = soup.find(id='user_list_table')

list_players = table.select('.txtR')

for n in list_players:
    print(n.get_text())