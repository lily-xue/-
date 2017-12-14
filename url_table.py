#coding:utf-8
class Url_table(object):
    """docstring for url_table"""
    def __init__(self):
        self.arg = []

    def update(self,url):
        self.arg.append(url)
        return self.arg