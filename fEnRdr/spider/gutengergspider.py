#!/usr/bin/env python
# encoding: utf-8
import aiohttp, asyncio
from lxml import etree, html
from io import StringIO

base_url = r'http://www.gutenberg.org/'

bookcount = 0

@asyncio.coroutine
def parse_book(subject,url):
    bookurl = base_url + 'ebook/'
    page = yield from aiohttp.get(url)
    page = yield from page.text()
    dom = etree.HTML(page)
    book = {}
    book['id'] = url.split('/')[-1]
    book['html'] = bookurl
   # print(dom.xpath(r'//*[@id="download"]/*//td[2]/a'))
    book['epub-images'] = bookurl + book['id'] + '.epub.images'
    book['epub-noimages'] = bookurl + book['id'] + '.epub.noimages'
    book['kindle-images'] = bookurl + book['id'] + '.kindle.images'
    book['kindle-noimages'] = bookurl + book['id'] + '.kindle.noimages'
    book['txt'] = bookurl + book['id'] + '.txt.utf-8'
    print(book)
    '''
    downloadurls = {}
    urls = dom.xpath(r'//*[@id="download"]/*//td[2]/a')
    for i in range(0, 6):
        print(urls[i].get('href'))
        downloadurls[urls[i].text] = urls[i].get('href')
    print(downloadurls)
    '''

@asyncio.coroutine
def parse_books(url):
    page = yield from aiohttp.get(url)
    page = yield from page.text()
    dom = etree.HTML(page)
    books = dom.xpath(r'//*[@id="mw-content-text"]/ul/li/a[@class="extiw"]')
    for book in books:
        print(book.text)
        print(book.get('href'))
        yield from parse_book(book.get('href'))

@asyncio.coroutine
def parse_subject(parent, url):
    count = 0
    page = yield from aiohttp.get(url)
    page = yield from page.text()
    dom = etree.HTML(page)
    subjects = dom.xpath(r'//*[@id="mw-pages"]/div/*//a')
    for subject in subjects:
        print(subject.text)
        print(subject.get('href'))
        yield from parse_books(base_url + subject.get('href'))
        count = count + 1
    print('total in' + str(count))

@asyncio.coroutine
def parse_category(urls):
    page = yield from aiohttp.get(urls);
    page = yield from page.text()
#    dom = etree.parse(StringIO(page), etree.HTMLParser())
#    title = dom.xpath('/html/head/title/text()')
    dom = etree.HTML(page)
    title = dom.xpath("//*[@id='mw-subcategories']/div/table/*/tr")
    categorys = dom.xpath(r'//*[@id="mw-subcategories"]/*//a')
    for category in categorys:
        print(category.get('href'))
        print(category.text)
        yield from parse_subject(category.text, base_url + category.get('href'))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    urls = ['http://www.gutenberg.org/wiki/Category:Bookshelf']
#    loop.run_until_complete(asyncio.wait([parse_category(url) for url in urls] ))
    loop.run_until_complete(parse_book('sss', url = 'http://www.gutenberg.org/ebooks/7190'))
    loop.close()





