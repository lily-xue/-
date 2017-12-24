#coding=utf-8
import urllib.request
import os, sys
def saveHtml(url,output_directory):
#    注意windows文件命名的禁用符，比如 /
	try:
		req = urllib.request.urlopen(url)
		html=req.read()
		# print(html)
		file_name=url.replace('/', '_').replace(":"," ")
		print(file_name)
		if(os.path.exists(output_directory)):
			pass
		else:
			os.mkdir(output_directory)
		
		with open(output_directory+'/'+file_name, "wb") as f:
		#   写文件用bytes而不是str，所以要转码
			f.write(html)
			print('download'+file_name+'successful')
		f.close()            
	except Exception as e:
		print(url)
		print("save HTML error:\n")
		print(e)
		
		#将列表中的url，且不在url_table中的url，保存到指定的文件夹中
def saveHtmllists(urls,output_directory,url_table):
	for url in urls:
		if url not in url_table:
			saveHtml(url,output_directory)

