#!/usr/bin/python
#coding:utf-8
import requests
from bs4 import BeautifulSoup
import json
import re

def main():
    headers = {
        "Authorization": "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6InNoZW50b3UxMjM0N0AxNjMuY29tIiwiaWF0IjoxNjA3NDE0MzgyLCJuYmYiOjE2MDc0MTQzODIsImV4cCI6MTYwNzQ1NzU4Mn0.lQF0KIweHLOyNEwB_9Ml_vzyO0svEsoQSTowd6diCEA"
    }
    url = "https://api.zoomeye.org/host/search?query=port:6379&page=1&facet=app,os"
    info = requests.get(url=url,headers=headers)
    r_decoded = json.loads(info.text)
    for line in r_decoded['matches']:
        print(line['ip']+': '+str(line['portinfo']['port']))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("interrupted by user, killing all threads...")


