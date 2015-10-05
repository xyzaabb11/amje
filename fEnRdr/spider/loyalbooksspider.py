#!/usr/bin/env python
# encoding: utf-8

import time
import asyncio, aiohttp
from lxml import etree, html
import sys
sys.path.append('../..')
from amje.wsgi import *
from fEnRdr.models import *

base_url = 'http://www.loyalbooks.com'

@asyncio.coroutine
def parse_book_content(book, txturl):
    bookcontent = BookContent.objects.using('fEnRdr').filter(book = book)
    if bookcontent:
        return
    page = yield from aiohttp.get(txturl)
    page = yield from page.text()
    bookcontent = BookContent.objects.using('fEnRdr').get_or_create(name = book.name, book = book, content = page)

@asyncio.coroutine
def parse_book(category, name, url):
    page = yield from aiohttp.get(url)
    page = yield from page.text()
    dom = etree.HTML(page)
    try:
        book = {}
        book['name'] = name
        book['image'] = base_url + dom.xpath(r'//*[@id="contentcolumn"]//img')[0].get('src')
        book['mainpage'] = url
        #path = dom.xpath(r'//*[@id="contentcolumn"]//font[1]/a')
        #if not path:
        #    path = dom.xpath(r'//*[@id="contentcolumn"]/div/div/table[1]//tr[2]/td/font/span')
        #book['author'] = path[0].text
        book['author'] = dom.xpath(r'//*[@class="book-author"]//*[@itemprop="author"]')[0].text
        descriptions = dom.xpath(r'//*[@id="contentcolumn"]//td//p')
        description = ''
        for des in descriptions:
            description = description + html.tostring(des, method='text',encoding='unicode')
        book['description'] = description
        #book['epub'] = base_url + dom.xpath(r'//*[@id="contentcolumn"]/div/div/table[2]//tr[2]/td[1]/a')[0].get('href')
        #book['kindle'] = base_url + dom.xpath(r'//*[@id="contentcolumn"]//tr[2]/td[2]/a')[0].get('href')
        #book['html'] = dom.xpath(r'//*[@id="contentcolumn"]/div/div/table[2]//tr[3]/td[1]/a')[0].get('href')
        #book['txt'] = base_url + dom.xpath(r'//*[@id="contentcolumn"]//tr[3]/td[2]/a')[0].get('href')
        book['epub'] = base_url + dom.xpath(r'//table[@summary="eBook Downloads for Kindle, Nook, Sony Reader, iPad and more"]//tr[2]/td[1]/a')[0].get('href')
        book['kindle'] = base_url + dom.xpath(r'//table[@summary="eBook Downloads for Kindle, Nook, Sony Reader, iPad and more"]//tr[2]/td[2]/a')[0].get('href')
        book['html'] = dom.xpath(r'//table[@summary="eBook Downloads for Kindle, Nook, Sony Reader, iPad and more"]//tr[3]/td[1]/a')[0].get('href')
        book['txt'] = base_url + dom.xpath(r'//table[@summary="eBook Downloads for Kindle, Nook, Sony Reader, iPad and more"]//tr[3]/td[2]/a')[0].get('href')
        #print(book['name'])
        cate = Category.objects.using('fEnRdr').get_or_create(name = category)[0]
        #print(cate.id)
        auth = Author.objects.using('fEnRdr').get_or_create(name = book['author'])[0]
        #print(type(auth))
        '''
        book_set = Book()
        book_set.name = book['name']
        print(type(book_set.name))
        book_set.category_id = cate.id
        book_set.cover = book['image']
        book_set.mainpage = book['mainpage']
        book_set.summary = book['description']
        book_set.epub = book['epub']
        book_set.kindle = book['kindle']
        book_set.html = book['html']
        book_set.txt = book['txt']
        print(book_set)
        book_set.save(using='fEnRdr')
        book_set.author.add((auth))
        '''
        book_set = Book.objects.using('fEnRdr').get_or_create(
                name = book['name'],
                category = (cate),
                cover = book['image'],
                mainpage = book['mainpage'],
                summary = book['description'],
                epub = book['epub'],
                kindle = book['kindle'],
                html = book['html'],
                txt = book['txt'],
                )[0]
        book_set.author.add((auth))
        #print(book_set)
        yield from parse_book_content(book_set, book['txt'])
    except Exception as e:
        with open('error_book.txt', 'a') as f:
            f.writelines(name + '\t\t\t: ' + url)

@asyncio.coroutine
def parse_genre(category, url):
    page = yield from aiohttp.get(url)
    page = yield from page.text()
    dom = etree.HTML(page)
    books = dom.xpath(r'//*[@id="contentcolumn"]/div/table[2]/*//div/a')
    print(url)
    if books:
        for book in books:
            print('[' + time.ctime() + ']' +book.text.strip() + '\n\t\t: ' + book.get('href'))
            yield from parse_book(category, book.text.strip(), base_url + book.get('href'))
    else:
        books = dom.xpath(r'//*[@id="contentcolumn"]/div/table[2]/*//a[2]')
        for book in books:
            print('[' + time.ctime() + ']' +str(book[0].text) + '\n\t\t: ' + book.get('href'))
            yield from parse_book(category, str(book[0].text), base_url + book.get('href'))
        books = dom.xpath(r'//*[@id="contentcolumn"]/div/table[3]/*//div/a')
        if books:
            for book in books:
                print('[' + time.ctime() + ']' +book.text.strip() + '\n\t\t: ' + book.get('href'))
                yield from parse_book(category, book.text.strip(), base_url + book.get('href'))

@asyncio.coroutine
def parse_genre_pages(category, url):
    page = yield from aiohttp.get(url)
    page = yield from page.text()
    dom = etree.HTML(page)
    genres = dom.xpath(r'//*[@id="contentcolumn"]/div/table[1]/*//td/div[1]/div/ul/text()')
    pages = genres[0].split(' ')[-1].split('\\')[0].strip()
    print('"' + pages + '"')
    if pages:
        for i in range(int(pages) + 1):
            yield from parse_genre(category, url + '?page=' + str(i))
    else:
        yield from parse_genre(category, url)

@asyncio.coroutine
def parse_genres(url):
    page = yield from aiohttp.get(url)
    page = yield from page.text()
    dom = etree.HTML(page)
    genres = dom.xpath(r'//*[@id="contentcolumn"]/div/div[2]/table[1]/*//a')
    for genre in genres:
        href = genre.get('href')
        cat_name = href.split('/')[-1]
        print(cat_name + '\t: ' + href)
        yield from parse_genre_pages(cat_name, base_url + href)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.run_until_complete(parse_genres('http://www.loyalbooks.com/genre-menu'))
#    loop.run_until_complete(parse_book('http://www.loyalbooks.com/book/moby-dick-by-herman-melville'))
    loop.close()
