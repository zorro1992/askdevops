import requests
import urllib3
import pprint

#Current weather
weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=München&appid={api}')



print(weather)
print(weather.json())

d = weather.json()

pprint.pprint(d)
