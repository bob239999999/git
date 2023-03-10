#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple web client, using URLLIB and basic parsing

@author: carlesm
'''
import urllib3
import bs4

class WebClient(object):

    def __init__(self) -> None:
        super(WebClient, self).__init__()
        self.data = None
        # We are going to parse this page, to improve our code, this should be a parameter
        # in the constructor, or the language should be, f. i.
        self.url = "https://www.99-bottles-of-beer.net/language-python-808.html"

    def get_web_page(self):
        # connect to url
        httppool = urllib3.PoolManager()
        result = httppool.request("GET", self.url)
        # print(result.status)
        # print(result.headers)
        # get URL content
        # store content
        self.html = result.data.decode('utf-8')
        # print(self.html)
        

    def search_html(self):

        # /html/body/div/div[3]/pre
        # search HTML received for 
        # what we look for
        soup = bs4.BeautifulSoup(self.html, features="html.parser")
        div_main = soup.find_all('div', attrs={ "id" : "main" })[0]
        return div_main.find_all('pre')[0]
        
    def parse_html(self, html):        
        # parse found data     
        data = html.text   
        return data

    def parse_web_page(self):
        # search for data in html
        # extract data from html
        # store data
        html = self.search_html()
        self.data = self.parse_html(html)
        

    def get_data(self):
        # get_web_page
        # parse_web_page
        # return data
        self.get_web_page()
        self.parse_web_page()
        return self.data


if __name__ == "__main__":
    client = WebClient()
    data = client.get_data()
    print(data)