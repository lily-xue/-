#coding=utf-8
import urllib.request
class Webpage_save(object):
    """docstring for Webpage_save"""
    def __init__(self, url):
    # super(Webpage_save, self).__init__()
        self.url=url
        pass
    def getHtml(url):
        html = urllib.request.urlopen(url).read()
        return html
    def saveHtml(file_name, file_content):
    #    注意windows文件命名的禁用符，比如 /
        with open(file_name.replace('/', '_') + ".html", "wb") as f:
        #   写文件用bytes而不是str，所以要转码
        f.write(file_content)
