import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Scraper:
    def __init__(self):
        # self.end_point = 'https://www.billboard.com/charts/hot-100/1996-06-09/'
        # self.soup = BeautifulSoup(urlopen(self.end_point), 'html.parser')
        with open('data.txt', mode='r') as file:
            self.content = file.read()
        self.soup = BeautifulSoup(self.content, 'html.parser')

    def get_list(self):
        songs = list()
        li = self.soup.findAll('li', {'class': 'lrv-u-width-100p'})
        for lis in li:
            children = lis.findAll("h3")
            for child in children:
                songs.append(child)
                print(child.text.strip())
