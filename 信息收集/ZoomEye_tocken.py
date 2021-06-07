#!/usr/bin/python
#coding:utf-8
import requests
import json

def main():
    username = input("username:")
    password = input("password:")
    url = "https://api.zoomeye.org/user/login"
    data = json.dumps({'username': username, 'password': password})
    access_key = requests.post(url=url,data=data,verify=False)
    print(access_key.text)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("interrupted by user, killing all threads...")



