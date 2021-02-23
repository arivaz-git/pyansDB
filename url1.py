import requests
#resp = requests.get("http://api.open-notify.org/astros.json")
ASTRO = "http://api.open-notify.org/astros.json"
resp = requests.get(ASTRO)
onsis = resp.json()
onsis 
