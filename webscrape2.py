# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:54:52 2020

@author: Alex
"""

import requests
import csv
import time
from bs4 import BeautifulSoup

url = "https://old.reddit.com/r/programminghumor/"
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
domains = soup.find_all("span", class_="domain")


for domain in domains:
    if domain != "(self.programminghumor)":
        continue

    print(domain.text)
    

attrs = {'class': 'thing', 'data-domain': 'self.programminghumor'}

    
counter = 1

while (counter <= 10):
    for post in domain:
        title = post.find('p', class_="title").text
        author = post.find('a', class_='author').text
        comments = post.find('a', class_='comments').text
        if comments == "comment":
            comments = 0
        likes = post.find("div", attrs={"class": "score likes"}).text
        if likes == "•":
            likes = "None"

        post_line = [counter, title, author, likes, comments]
        with open('output.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(post_line)

    counter += 1
    next_button = soup.find("span", class_="next-button")
    next_page_link = next_button.find("a").attrs['href']
    time.sleep(2)
    page = requests.get(next_page_link, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')