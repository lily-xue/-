#coding:utf-8

from docopt import docopt
from config_load import Config_load
import argparse
from seedfile_load import Seedfile_load
from webpage_parse import Webpage_parse
if __name__ == '__main__':
    parser=argparse.ArgumentParser(description="this is a mini spider for crawl html")
    parser.add_argument("-c",metavar='file_name',type=argparse.FileType('r'),help="**.conf,some conf about spider")
    parser.add_argument("-v",action='version', version='mini_spider 1.0')
    args=parser.parse_args()
    # 以字典形式返回爬虫配置
    c=Config_load(args.c.name)
    print('your spider config is :\n',c.config)
    urls=Seedfile_load.get_urls(c.config['url_list_file'])
    print('read urls:\n',urls)

    Webpage_parse.parse('http://www.hinabian.com',c.config['crawl_interval'],c.config['crawl_timeout'],c.config['target_url'])