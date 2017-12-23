#coding:utf-8
import os
class Url_unvisited(object):
    def __init__(self,level,url):
        self.level=level
        self.url=url

def get_urls(file):
    url_lists_unvisited=[]
    try:
        f=open(file,'r')
        lines=f.readlines()
        for line in lines:
            print(url_unvisited)
            url_unvisited=Url_unvisited(0,line.strip())
            url_lists_unvisited.append(url_unvisited)
    except FileNotFoundError:
        print('file not exist')
    return url_lists_unvisited
