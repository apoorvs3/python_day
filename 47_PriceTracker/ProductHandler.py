import logging
from urllib.request import urlopen
import requests
from lxml import etree
from bs4 import BeautifulSoup

HEADERS_ = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/110.0.0.0 Safari/537.36',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}


class product:
    def __init__(self):
        self.soup = None
        self.response = requests.get(
            url='https://www.amazon.com/MSI-GeForce-RTX-3060-12G/dp/B08WPRMVWB/ref=sr_1_3?crid=27PCAR5AH8GNZ&keywords'
                '=nvidia+3060&qid=1677847816&sprefix=%2Caps%2C274&sr=8-3',
            headers=HEADERS_
        )
        # logging.debug(f'Amazon page something like /n {self.response.text}')

    def create_soup(self):
        self.soup = BeautifulSoup(f'{self.response.content}', 'html.parser')
        dom = etree.HTML(str(self.soup))
        price = dom.xpath('/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div/div[1]/div[3]/div[1]/span[2]/span[1]')[0].text
        return float(price[1:])
