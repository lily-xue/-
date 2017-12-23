#!/usr/bin/env python
#coding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
class Webpage_parse(object):
    """docstring for Webpage_parse.py"""
    def __init__(self, arg):
        pass
    
    def parse(url,target_url):
        out_urls=[]
<<<<<<< HEAD
        #max_depth=int(max_depth)
        #crawl_timeout=int(crawl_timeout)
=======
        # max_depth=int(max_depth) 
        # crawl_timeout=int(crawl_timeout)
>>>>>>> aea87110a8d1472e309475d215422b2934d0ca19
        # if(max_depth,crawl_timeout >=0):
        #     print('argument ok')
        # else:
        #     print('argument ilegal')
<<<<<<< HEAD
        #
=======
        
>>>>>>> aea87110a8d1472e309475d215422b2934d0ca19
        reseponse=urlopen(url)
        html=reseponse.read()
        soup = BeautifulSoup(html, "html.parser")
        parse_urls = soup.find_all("a")
        for parse_url in parse_urls:
            parse_url=parse_url.get('href')
            # print(target_url)
            print(parse_url)
            try:
                if(re.match(target_url,parse_url) and re.match('/',parse_url)):
                    parse_url=url+parse_url
                    if(parse_url not in out_urls):
                        print(parse_url)
                        out_urls.append(parse_url)
                elif(re.match(target_url,parse_url) and (parse_url not in out_urls) ):
                    print(parse_url)
                    out_urls.append(parse_url)
            except Exception as e:
                print('Tt is not target url')
        print(out_urls)
        return out_urls
   