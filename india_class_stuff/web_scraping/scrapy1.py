from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.niitahmedabad.com/")
gn=BeautifulSoup(html.read(),"lxml");
print(gn.h1)
#print(gn.get_text())
print(gn.title)
print(gn.head)
print(gn.title.text())
print(gn.table)
print(gn.table.get_text())
print(gn.p.text())
print(gn.body.text())

