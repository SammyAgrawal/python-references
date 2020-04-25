from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
r = urlopen('https://www.niitmaninagar.com/contact.php')
soup = BeautifulSoup(r.read(),'lxml')
iframes = soup.find_all("iframe")



for frame in iframes:
    
    response =urlopen(frame.attrs['src'])
 
    iframe_soup = BeautifulSoup(response,'lxml')
   
    m=str(iframe_soup)

    pattern=re.compile("[0-9][0-9][.]\d+[,][0-9][0-9][.]\d+")

    tuples = [(m.start(0), m.end(0)) for m in re.finditer(pattern, m)]

    counter = tuples[2][0]

    found = False
    started = False
    newString = ""
    while not found:
       
        if started:
            
            if m[counter] == '"':
               
                break
                
            else:
                newString+=m[counter]
                
             
            
        else:
            if m[counter] == '"':

                started = True
        counter-=1
    print(newString[::-1])



    
