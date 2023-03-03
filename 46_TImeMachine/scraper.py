import logging
import ssl

import certifi
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging


class Scraper:
    def __init__(self, dob: str):
        self.end_point = f'https://www.billboard.com/charts/hot-100/{dob.strip()}/'
        logging.info(f'url is {self.end_point} and its type is {type(self.end_point)}')
        self.soup = BeautifulSoup(urlopen(self.end_point, context=ssl.create_default_context(cafile=certifi.where())), 'html.parser')
        # with open('data.txt', mode='r') as file:
        #     self.content = file.read()
        # self.soup = BeautifulSoup(self.content, 'html.parser')

    def get_list(self):
        songs = list()
        li = self.soup.findAll('li', {'class': 'lrv-u-width-100p'})
        for lis in li:
            children = lis.findAll("h3")
            for child in children:
                songs.append(child.string.strip())
        logging.info(f"songs are : {songs}")
        return songs

