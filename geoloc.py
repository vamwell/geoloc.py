# Script written by vamwell 3/7/21
import requests
from os import system, name

def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

clear()
print("Enter IP Below (example: 1.1.1.1)\nOr Leave Empty To Geolocate Your IP.")
ip = input(">> ")
clear()
r = requests.get("http://ip-api.com/json/" + ip + "?fields=1245183")
# I know this is ugly, but it works.
print("IP:           " + r.json()['query'])
print("Continent:    " + r.json()['continent'])
print("Country:      " + r.json()['country'])
print("Country Code: " + r.json()['countryCode'])
print("Timezone:     " + r.json()['timezone'])
print("City:         " + r.json()['city'])
print("Zip:          " + r.json()['zip'])
print("ISP:          " + r.json()['isp'])
print("Lat:          " + str(r.json()['lat']))
print("Lon:          " + str(r.json()['lon']))
print("Reverse DNS:  " + r.json()['reverse'])
print("Proxy:        " + str(r.json()['proxy']))
