import requests
from bs4 import BeautifulSoup
import json


url ="https://tutorialsninja.com/demo/"

response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")

pagetitle=soup.title.string if soup.title else "No title"

print(pagetitle)

for link in soup.find_all("a"):
    href=link.get("href")
    print(href)