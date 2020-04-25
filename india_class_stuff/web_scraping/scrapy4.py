import requests
import urllib.request
from bs4 import BeautifulSoup

url="https://www.w3schools.com/html/html_tables.asp"

r=requests.get(url)

content=r.text
gj=BeautifulSoup(content,"html.parser")

for tr in gj.find_all('tr')[2]:
         tds=tr.find_all('td')
         print("value:%s","value2:%s","value3:%s" (tds[0].text,tds[1].text,tds[2].text))
         
