import logging
import ssl

import certifi
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


class BrowserHandler:
    def __init__(self):
        self.values = dict()
        self.soup = BeautifulSoup(
            urlopen('https://myhttpheader.com/', context=ssl.create_default_context(cafile=certifi.where())),
            'html.parser')

    def get_properties(self):
        rows = self.soup.findAll('div', {'class': 'row'})
        logging.info(f'{len(rows)} are recovered from the site')
        for label in rows:
            label_ = label.find('div', {'class': 'label'}).string.replace(':', '').strip()
            value_ = label.find('div', {'class': 'out'}).string.strip()
            self.values[label_] = value_
        return self.values
