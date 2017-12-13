#coding:utf-8
import os
class Seedfile_load(object):
    """docstring for Seedfile_load"""
    def __init__(self):
    #super(Seedfile_load, self).__init__()
        pass
    def get_urls(file):
        url_lists=[]
        try:
            f=open(file,'r')
            lines=f.readlines()
            for line in lines:
                url_lists.append(line.strip())
        except FileNotFoundError:
            print('file not exist')
        return url_lists
