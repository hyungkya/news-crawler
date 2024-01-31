import requests
import os

header = {
    "Content-Type": "application/json; charset=UTF-8",
    "X-Naver-Client-Id": os.environ.get("X-Naver-Client-Id"),
    "X-Naver-Client-Secret": os.environ.get("X-Naver-Client-Secret"),
}

option = {
    "query": "000270",
    "display": 100,
    "start": 1,
    "sort": "date"
}

url = ("https://openapi.naver.com/v1/search/news.xml?query={query}&display={display}&start={start}&sort={sort}"
       .format(query=option['query'],
               display=option['display'],
               start=option['start'],
               sort=option['sort']))

response = requests.get(url, headers=header)

with open("links.xml", "w") as f:
    f.write(response.text)
