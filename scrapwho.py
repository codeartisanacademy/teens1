from selenium import webdriver
import requests

req = requests.get('https://www.who.int/emergencies/diseases/novel-coronavirus-2019')

driver = webdriver.PhantomJS()

driver.get('https://www.who.int/emergencies/diseases/novel-coronavirus-2019')