import urllib.request
import json
ASTRO = "http://api.open-notify.org/astros.json"

def main():
    resp = urllib.request.urlopen(ASTRO).read()
    #resp = resp.read()
    respstr = resp.decode("utf-8")
    oniss = json.loads(respstr)
    print(oniss.get("people"))

if __name__ == "__main__":
    main()
