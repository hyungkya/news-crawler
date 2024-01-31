import requests
from bs4 import BeautifulSoup
import re


def request(url):
    header = {"Content-Type": "application/json; charset=UTF-8"}
    response = requests.get(url, headers=header)
    if not ('charset' in response.headers['content-type']):
        response.encoding = response.apparent_encoding
    return response


def parse_article(response):
    elements = BeautifulSoup(response.content, 'html.parser')
    if 'n.news.naver.com' in response.request.url:
        return elements.find("article").text
    elif 'edaily.co.kr' in response.request.url:
        return elements.find("div", "xforms").text
    elif 'seoul.co.kr' in response.request.url:
        return elements.find("div", "v_article").text
    else:
        return None


def split_article_into_sentences(article: str):
    pattern = re.compile("[가-힣][.][^\\n]")

    while x := re.search(pattern, article):
        article = article[:x.end() - 1] + "\n" + article[x.end() - 1:]

    return [x.strip() for x in article.split("\n") if len(x.strip()) > 0]


def url_changer(url: str):
    if url.startswith("https://www.edaily.co.kr"):
        return url.replace("read", "print")
    else:
        return url


def request_and_parse(url: str):
    changed_url = url_changer(url)
    response = request(changed_url)
    article = parse_article(response)
    if article is not None:
        return split_article_into_sentences(article)
    else:
        return []