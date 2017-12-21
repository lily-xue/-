#coding=utf-8
import threading
import time
import queue
from webpage_parse import Webpage_parse
from Webpage_save import Webpage_save
from url_table import Url_table

class Crawl_thread(threading.Thread):
	"""docstring for Crawl_thread"""
	def __init__(self,ThreadID):
		#super(Crawl_thread, self).__init__()
		self.ThreadID=ThreadID
		self.count = 0

	def run(q,url_table,crawl_level,target_url,output_directory):
		print(self.ThreadID)
		while not q.empty():
			item=q.get()
			if (item.level <= crawl_level) and (item.url not in url_table):
				url_lists=Webpage_parse.parse(item.url,target_url) 
				for url in url_lists:
					if url not in url_table:
						Webpage_save.saveHtml(url,output_directory)
						print("save successful")
				url_table.append(item.url)
				print("add url to table:"+item.url)
				url_list_level=item.level+1
				if url_list_level<=crawl_level:
					for url in url_lists:
						if url not in url_table:
							urlitem=Urlitem(url,url_list_level)
							list_add_item(q,urlitem)

#定义url队列元素，含有url和等级
class Urlitem(object):
	def __init__(self,url,level):
		self.url=url
		self.level=level

#定义函数，给队列增加元素
def list_add_item(q,urlitem):
	print(urlitem.url)
	q.put(urlitem)
	print(q.qsize())

#定义函数，从队列弹出元素
def list_delete_item(q):
	while not q.empty():
		print(q.get().url)
		print(q.qsize())
		print("*****")
# #定义从队列爬取函数，更新url_table和q
# def crwal_from_queue(q,url_table,crawl_level,target_url,output_directory):
# 	while not q.empty():
# 		item=q.get()
# 		if (item.level <= crawl_level) and (item.url not in url_table):
# 			url_lists=Webpage_parse.parse(item.url,target_url) 
# 			for url in url_lists:
# 				if url not in url_table:
# 					Webpage_save.saveHtml(url,output_directory)
# 					print("save successful")
# 			url_table.append(item.url)
# 			print("add url to table:"+item.url)
# 			url_list_level=item.level+1
# 			if url_list_level<=crawl_level:
# 				for url in url_lists:
# 					if url not in url_table:
# 						urlitem=Urlitem(url,url_list_level)
# 						list_add_item(q,urlitem)
# 						# prn(url_table)
b=Urlitem('http://www.baidu.com',0)
c=Urlitem('http://www.qq.com',0)
c=Urlitem('http://www.hinabian.com',0)
q=queue.Queue()
q.put(b)	
q.put(c)	
url_table=[]
#crwal_from_queue(q,url_table,3,'.*.(htm|html)$','./output')

thread1=Crawl_thread(1)
thread2=Crawl_thread(2)

