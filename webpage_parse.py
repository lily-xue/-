#!/usr/bin/env python
#coding:utf-8
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
#删除列表中的javascrip
def del_javascript(urls):
	for u in urls:
		if (re.match('javas*',u)):
			print(u)
			urls.remove(u)
			print("remove"+u)
	print("delete javascript urls number:",len(urls))
	return(urls)

def url_protocol(url):
	'''
	获取输入的url地址的协议，是http、https等
	'''
	print('该站使用的协议是：' + re.findall(r'.*(?=://)',url)[0])
	return re.findall(r'.*(?=://)',url)[0]

def del_protocol(urls):
	no_pro_urls=[]
	for url in urls:
		if re.match('.*(?=://)',url):
			url=url.split('://')[1]
			no_pro_urls.append(url)
		else:
			no_pro_urls.append(url)
	return no_pro_urls
def parse(url,target_url,time):
	out_urls=[]
	# max_depth=int(max_depth) 
	# crawl_timeout=int(crawl_timeout)
	# if(max_depth,crawl_timeout >=0):
	#     print('argument ok')
	# else:
	#     print('argument ilegal')
	
	reseponse=urlopen(url,timeout=time)
	html=reseponse.read()
	soup = BeautifulSoup(html, "html.parser")
	parse_urls = soup.find_all("a")
	for parse_url in parse_urls:
		parse_url=parse_url.get('href')
		try:
			#给相对路径的链接加上头部
			if(re.match(target_url,parse_url) and re.match('/',parse_url)):
				parse_url=url+parse_url
				#判断该urls是否已经在列表中
				if(parse_url not in out_urls):
					print(parse_url)
					out_urls.append(parse_url)
			#如果匹配上，且url不在列表中，直接添加到列表中
			elif(re.match(target_url,parse_url) and (parse_url not in out_urls) ):
				print(parse_url)
				out_urls.append(parse_url)
		except Exception as e:
			print('Tt is not target url')
	print("urls number :",len(out_urls))
	return out_urls


url='http://www.hinabian.com'
protocol=url_protocol(url)
new_url_list=parse(url,'.*.(htm|html)$',1)
list_no_javascript=del_javascript(new_url_list)
no_pro=del_protocol(list_no_javascript)
print(no_pro)


