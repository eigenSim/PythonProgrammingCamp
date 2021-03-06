#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:53:09 2017

@author: yoon
"""

# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

req = requests.get('http://www.melon.com/chart/index.htm')
html = req.content
soup = BeautifulSoup(html, 'lxml') # pip install lxml
list_song = soup.find_all(name="div", attrs={"class":"rank01"})
list_artist = soup.find_all(name="div", attrs={"class":"rank02"})

# 곡명 추출
for index in range(0, len(list_song)):
    title = list_song[index].find('a').text
    print(index+1, ' : ', title)
    if index == 100:
        break

# 피처링 제거
for index in range(0, len(list_song)):
    title = list_song[index].find('a').text
    print(index+1, ' : ', title.split("(")[0])
    if index == 100:
        break

# csv로 저장
import csv

with open('melon_chart.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['rank', 'song', 'artist'])
    for index in range(0, len(list_song)):
        title = list_song[index].find('a').text
        artist = list_artist[index].find('a').text
        writer.writerow([index+1, title, artist])
        if index == 100:
            break

# 저장된 파일 pd로 읽기
import pandas as pd
datas = pd.read_csv('melon_chart.csv')