#coding=utf-8
import threading
import time
import queue
from webpage_parse import Webpage_parse
import Webpage_save
from url_table import Url_table

class Crawl_thread(threading.Thread):
	"""docstring for Crawl_thread"""
	def __init__(self,ThreadID,crawl_level,target_url,output_directory):
		super(Crawl_thread, self).__init__()
		self.ThreadID=ThreadID
		self.count = 0
		self.crawl_level=crawl_level
		self.target_url=target_url
		self.output_directory=output_directory

	def run(self):
		print(self.ThreadID)
		while not q.empty():
			item=q.get()
			if (item.level <= self.crawl_level) and (item.url not in url_table):
				url_lists=Webpage_parse.parse(item.url,self.target_url)
				Webpage_save.saveHtmllists(url_lists,self.output_directory,url_table)
				url_table.append(item.url)
				print("add"+item.url+"url to table")
				#当前item等级<爬取等级，要将爬取到的urllist加入q中，并记录level
				if (item.level < self.crawl_level):
					url_list_level=item.level+1
					#将下一个待爬取的list加入q中
					q_add_item_list(q,url_list_level,url_lists)
			print("pop "+item.url+"success")
			
#定义url队列元素，含有url和等级
class Urlitem(object):
	def __init__(self,url,level):
		self.url=url
		self.level=level

#定义函数，给q增加元素
def q_add_item(q,urlitem):
	print(urlitem.url)
	q.put(urlitem)
	print(q.qsize())
	
#将urllist添加到q中
def q_add_item_list(q,level,url_lists):
	for url in url_lists:
		item=Urlitem(url,level)
		q_add_item(q,item)

#定义函数，从队列弹出元素

def list_delete_item(q):
	while not q.empty():
		print(q.get().url)
		print(q.qsize())
		print("*****")

b=Urlitem('http://www.baidu.com',0)
c=Urlitem('http://www.qq.com',0)
c=Urlitem('http://www.hinabian.com',0)
q=queue.Queue()
q.put(b)	
q.put(c)	
url_table=[]
#crwal_from_queue(q,url_table,3,'.*.(htm|html)$','./output')

thread1=Crawl_thread(3,3,'.*.(htm|html)$','./output')
thread2=Crawl_thread(4,3,'.*.(htm|html)$','./output')
thread1.start()
thread1.start()
thread1.join()
thread2.join()
print("end")

