import xml.etree.ElementTree as ET
import visitor
import pandas as pd

sentences = []
tree = ET.ElementTree(file="links.xml")

for item in tree.findall("./channel/item"):
    sentences.extend(visitor.request_and_parse(item.find("link").text))

df = pd.DataFrame(sentences, columns=["sentence"])
df.insert(1, "sentiment", -1, True)
df.to_csv("sentences.csv", index=False)

