import socket
import threading
import os
import requests
import json
import pickle
import schedule
import time
import requests as req

from datetime import datetime
from requests.structures import CaseInsensitiveDict

def update_json_file():
    url = 'https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now'
    r = requests.get(url)
    r = r.text.encode("UTF8")
    data = json.loads(r)
    file_data = open('data.json', 'wb')
    file_data.write(r)
    file_data.close()

def get_api():
    #Lấy api_key một cách tự động do sau 15 ngày sẽ phải cập nhật
    url_get_api_key = "https://vapi.vnappmob.com/api/request_api_key?scope=exchange_rate"
    resp = req.get(url_get_api_key)
    api_key = resp.text[12:(len (resp.text) - 3)]

    url = "https://vapi.vnappmob.com/api/v2/exchange_rate/vcb"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    #api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzgyMDIxMzYsImlhdCI6MTYzNjkwNjEzNiwic2NvcGUiOiJleGNoYW5nZV9yYXRlIiwicGVybWlzc2lvbiI6MH0.YS1yDCiew3Lo0tABSSlPpqTK_xHr_iQzGP3wHPJnPII"
    headers["Authorization"] = "Bearer " + api_key

    r = requests.get(url, headers=headers)
    r = r.text.encode("utf-8")#Dữ liệu text kiểu binary
    data = json.loads(r)#Convert from json to python

    #Ghi file binary
    file_data = open("inforExchange.json", "wb")
    file_data.write(r)
    file_data.close()

get_api()