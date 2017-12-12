#coding:utf-8
#读取配置文件
def config_load(conf_file):
    f=open(conf_file,'r')
    lines=f.readlines()
    f.close()
    print(lines)
    return lines
