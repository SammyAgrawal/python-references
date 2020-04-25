import csv
import urllib.request
from bs4 import BeautifulSoup
f=open('gunjan.csv','w',newline='')  #Comma-Separated Value-Variable
writer=csv.writer(f)
gj=BeautifulSoup(urllib.request.urlopen("https://en.wikipedia.org/wiki/Global_music_industry_market_share_data").read(),'lxml')
tbody=gj('table',{"class":"wikitable plainrowheaders sortable"})[0].find_all('tr')
print (tbody)
for row in tbody:
         col=row.findChildren(recursive=False) # no repeat in data
         col=[ele.text.strip() for ele in col]
         writer.writerow(col)
         print(col)
f.close()         
         
