import requests
import json
from urllib.request import urlopen

ip_request = requests.get('https://get.geojs.io/v1/ip.json')
ipAdd = str(ip_request.json()['ip'])

url = 'http://api.db-ip.com/v2/free/'+ipAdd
response = urlopen(url)
data = json.load(response)
print(ipAdd)
print(data['city'])