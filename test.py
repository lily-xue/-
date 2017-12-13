#coding:utf-8
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",type=int)
#不加type=int的话,argparse会将输入当作字符串处理
args = parser.parse_args()
print (args)