import requests as req # type: ignore
from pprint import pprint

# get my ip address and convert it to json (dict)
ip = req.get('https://api.ipify.org/?format=json').json()

# get info about geolocation of that ip and convert it to json (dict)
geoLocation = req.get('https://ipinfo.io/{}/geo'.format(ip['ip'])).json()

# print info
pprint(geoLocation)



