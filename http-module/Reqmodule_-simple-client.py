from urllib import request
import requests

url = "http://127.0.0.1:2017/getauto"

res = requests.get(url)

print(res.json())
