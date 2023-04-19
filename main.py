import requests
from bs4 import BeautifulSoup
from lxml import etree


def parse_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    html = etree.HTML(str(soup))
    for item in html.xpath('//*[@itemprop="image"]'):
        if item.get('src'):
            return item.get('src')

if __name__ == '__main__':
    print(parse_page('url to soundcloud'))