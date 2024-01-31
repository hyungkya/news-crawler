import requests
import os
import xml.etree.ElementTree as ET
import visitor
import pandas as pd

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

sentences = []
tree = ET.ElementTree(file="links.xml")

for item in tree.findall("./channel/item"):
    sentences.extend(visitor.request_and_parse(item.find("link").text))

df = pd.DataFrame(sentences, columns=["sentence"])
df.insert(1, "sentiment", -1, True)
df.to_csv("sentences.csv", index=False)