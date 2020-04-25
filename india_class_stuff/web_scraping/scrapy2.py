from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.niitmaninagar.com/")
gn=BeautifulSoup(html.read(),"lxml");
gn2=gn.find_all("h1")
#print(gn2)

for i in gn2:
         print(i.text)




