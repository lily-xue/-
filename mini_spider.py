#coding:utf-8
'''定向网页抓取器说明
Usage:
    mini_spider.py -c <spider.conf> 
    mini_spider.py -h|v

Options:
    -c 抓取配置文件
    -v 版本
    -h 帮助文档

Example:
    mini_spider.py -c spider.conf

'''
from docopt import docopt
from config_load import config_load
import argparse

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description="this is a mini spider for crawl html")
    parser.add_argument("-c",metavar='file_name',type=argparse.FileType('r'),help="**.conf,some conf about spider")
    parser.add_argument("-v",action='version', version='mini_spider 1.0')
    args=parser.parse_args()
    # for line in args.file:
    #     print(line)
    print(args.c)
    print(name)
    arguments = docopt(__doc__, version='1.0')
    # print(arguments)
    # print(arguments['-c'])
    config_load(arguments['-c'])
