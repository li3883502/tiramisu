from bs4 import BeautifulSoup
import requests


def tsdouban(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit'
                             '/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup


def get_page(url):
    href = []
    soup = tsdouban(url)
    page = soup.select('div.paginator a')
    for i in page:
        href.append(i['href'])
    return href


def get_ins(url):
    ins = {}
    soup = tsdouban(url)
    books = soup.select('td[valign="top"]')
    for i, ele in enumerate(books):
        if i == 0 or i % 2 == 0:
            continue
        else:
            # print(ele)
            title = ele.select('a[title]')[0]
            str = ''
            for j in title.stripped_strings:
                str += j
            if ele.select('span.inq'):
                inq = ele.select('span.inq')[0].string
            else:
                inq = ''
            ins[str] = [ele.select('p.pl')[0].string, ele.select('span.rating_nums')[0].string,
                         inq]
    return ins



def main():
    all_book = get_ins('https://book.douban.com/top250?start=0')
    href = get_page('https://book.douban.com/top250?start=0')
    print(href)
    for ele in href:
        new = get_ins(ele)
        all_book = dict(all_book, **new)
    return all_book


print(main())
