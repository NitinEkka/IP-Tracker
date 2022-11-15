import requests
import json
from urllib.request import urlopen
from geopy.geocoders import ArcGIS

ip_request = requests.get('https://get.geojs.io/v1/ip.json')
ipAdd = str(ip_request.json()['ip'])

url = 'http://api.db-ip.com/v2/free/'+ipAdd
response = urlopen(url)
data = json.load(response)
print(ipAdd)
city = data['city']
nom = ArcGIS()
city_coor = nom.geocode(city)
print(city_coor)
splitted = city_coor[0].split(", ")
max_len = int(len(splitted))
index = max_len - 2
city_name = splitted[index]
print(city_name)
