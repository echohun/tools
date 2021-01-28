# -*- coding: UTF-8 -*-
from urllib.parse import urlparse
from enum import Enum

###
###字体颜色处理函数(windows cmd中无效)
###如打印红色文字
###print_color('Hello World', fg = Color.RED.value)
###

class Color(Enum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
def print_color(text: str, fg: Color = Color.BLACK.value):
    print(f'\033[{fg}m{text}\033[0m')

###
###url检测函数
###需根据情况自行构造，如检测漏洞页面是否存在等操作,windows cmd下建议注释print_color函数，自行修改输出
###check_url(url)
###


def check_url(url):
    try:
        #使用url进行某些检测
        #需要自己写的部分
        if(1==1):#存在漏洞条件
            print("[success]存在xx漏洞")
            print_color(url,fg=Color.GREEN.value)
    except Exception as e:
        print("[error]不存在xx漏洞")
        print_color(url,fg=Color.RED.value)
        pass
    return 0

###
###url处理函数
###从ip:port、http://ip:port、https://domain:port/path/xx.html等不同格式转化为 协议+ip/domain+port格式
###read_url
###


def read_url():
    f = open("urls.txt", 'r')
    for line in f.readlines():
        target = line.strip()
        #print(target)
        if "http" not in line:
            target="http://"+target
        target=urlparse(target.strip())
        #print(target)
        url = target.scheme+"://"+target.netloc
        print(url)
        #拼接成需要的格式
        check_url(url)


def main():
    read_url()

main()
