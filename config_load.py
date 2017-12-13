#coding:utf-8
#读取配置文件
class Config_load(object):

    def __init__(self, conf_file):
        #super(config_load, self).__init__()
        self.config={
        'url_list_file':'./urls',
        'output_directory':'./output',
        'max_depth':1,
        'crawl_interval':1,
        'crawl_timeout':1,
        'target_url':'.*.(htm|html)$',
        'thread_count':8
        }
        keys=self.config.keys()
        f=open(conf_file,'r')
        lines=f.readlines()
        for line in lines:
        #对每一行读取的内容进行处理，全部变成小写，去掉前后空格，去掉
            new_line=line.lower().strip().rstrip(';').split(':')
            #print(new_line)
            if(new_line[0] in keys):
                self.config[new_line[0]]=new_line[1].strip()
        #print('your spider config is :\n',self.config)
        f.close()
        #print(lines)
        #return lines
    #def getconfig(self,conf_file):

