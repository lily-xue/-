#coding=utf-8
import threading
import time
class Crawl_thread(threading.Thread):
	"""docstring for Crawl_thread"""
	def __init__(self,target, arg):
		super(Crawl_thread, self).__init__()
		self.target=target
		self.arg = arg
    
    def run(self):
        self.target(self.arg)