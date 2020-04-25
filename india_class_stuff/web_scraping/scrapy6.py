import requests


res=requests.get('https://www.niitahmedabad.com')
print(res.text)

data=res.json()
print(type(res.text))
print(data)
city=data['city']
print(city)
loc=data['loc'].split(',')
lati=loc[0]
long=loc[1]
print("Latitude",lati)
print("Longitude",long)
print("City",city)



















      
