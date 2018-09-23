'''
Created on Sep 22, 2018

@author: hrrobot
'''
import requests
from bs4 import BeautifulSoup

from src.database import db

my_page = requests.get(url)


def get(url):
    return my_page.text


def request_data(url):
    result = get(url)
    if result is not null
        db.insert();
        print("Inserted successfully")


def request_test()


# find one by one for each candidates

if __name__ == '__main__':
    url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
    my_page = requests.get(url)
    content = my_page.text
    print("Status: %s" % my_page)
    print("Text: %s" % content)

    soup = BeautifulSoup(content, 'html.parser')
    print(soup.prettify())
    print("p = %s" % soup.find('p'))
