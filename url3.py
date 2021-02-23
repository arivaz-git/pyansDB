#!/usr/bin/python3
import requests
"""
Created by : Arivaz
Dated : 22nd Feb 2021
"""
#python -m pip install requests
#https://api.nasa.gov/  to get api key
import json
NASA = "https://api.nasa.gov/planetary/apod"
def main():
    #get our API key into the program
    #read it ut f file
    #with open("E:\pyansDB\api.txt","r") as ncreds:
    with open(r"E:\pyansDB\api.txt","r") as ncreds:
        nc = ncreds.read()
    #make the API lookup
    #r = requests.get(f"[NASA]+"?api_key=nc)")
    r = requests.get(f"{NASA}?api_key={nc}")
    #if we got back a 200 resp
    if r.status_code == 200:
        #grab JSN off of the 200 resp
        #nj = ncreds.read()
        nj = r.json()
        #prin date
        print(nj.get("date"))
        #print explanation
        print(nj.get("explantion"))
        #print url
        print("url","no url")
    else:
        print("sorry, status is not 200 API service is down")
  
if __name__ == "__main__":
    main()
    input("press enter")
