from bs4 import BeautifulSoup
import requests
import re


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit'
                             '/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
url = 'https://book.douban.com/top250?start=0'

resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.text, 'lxml')

title = soup.select('div.pl2 > a')
se_title = soup.select('div.pl2 > a > span')
author = soup.select('p.pl')
star = soup.select('spen.rating_nums')
inq = soup.select('spen.inq')
next_page = soup.select('div.paginator > a')
for i in title:
    for j in i.strings:
        print(j)

print(type(soup.find_all('a', title="三体")[0].text))
