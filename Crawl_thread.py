#coding=utf-8
from url_table import Url_table
import threading
import time
#url对象，存储url和所在的层级
class Url(object):
    def __init__(self,url, level):
        self.url=url
        self.level = level

Uncrawl_urls=[]

def update_uncrawl_list(Url):
    Uncrawl_urls=Uncrawl_urls.append(Url)
    return Uncrawl_urls
#未爬取的url列表
Uncrawl_urls=Url('www.sina.com',0)

#已经爬取的url列表
url_table=Url_table()
url_table.update('www.hinabian.com')
print (Uncrawl_urls.url)
print(url_table.arg)

