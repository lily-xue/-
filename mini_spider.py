#coding:utf-8

from docopt import docopt
from config_load import Config_load
import argparse
from seedfile_load import Seedfile_load
from webpage_parse import Webpage_parse
from Webpage_save import Webpage_save
from url_table import Url_table



if __name__ == '__main__':
    parser=argparse.ArgumentParser(description="this is a mini spider for crawl html")
    parser.add_argument("-c",metavar='file_name',type=argparse.FileType('r'),help="**.conf,some conf about spider")
    parser.add_argument("-v",action='version', version='mini_spider 1.0')
    args=parser.parse_args()
    # 以字典形式返回爬虫配置
    c=Config_load(args.c.name)
    print('your spider config is :\n',c.config)
    #获取种子url
    urls_for_crawl=get_urls(c.config['url_list_file'])
    #print('read urls:\n',seed_urls)
    #初始化已抓取列表
    url_table=Url_table()
    print("crawld list:",url_table.arg)
    for seed in urls_for_crawl:
        #抓取和解析网页
        htmls=Webpage_parse.parse(seed,c.config['target_url'])                
        for html in htmls:
            if(html not in url_table.arg):
                #下载网页
                Webpage_save.saveHtml(html,c.config['output_directory'])
                url_table.update(html)
                #print(url_table.arg)

