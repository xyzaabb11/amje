#!/usr/bin/env python
# encoding: utf-8

import aiohttp, asyncio
import io, sys, os, time
import bs4
import re
import logging; logging.basicConfig(level = logging.INFO)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

@asyncio.coroutine
def parse_url(url):
    print(url)
    page = yield from aiohttp.get(url)
    print(page)
    page = yield from page.text()

loop = asyncio.get_event_loop()
urls = ['http://gutenberg.net.au/ebooks02/0200161.txt',]
loop.run_until_complete(parse_url(urls))
loop.close()
