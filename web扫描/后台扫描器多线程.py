#! -*- encoding:utf-8 -*-
# python3


import requests
from threading import Thread


def guesshtml(url,real_list):
    r = requests.get(url, timeout=30)
    if r.status_code==200:
        print("存在: "+url)
        real_list.append(url)
    else:
         print("不存在: %s 错误代码: %d"% (url,r.status_code))
    return real_list

def add_url(html,dic,url_list):
    for line in dic:
        line = line.replace('\n','')
        url = html + line
        url_list.append(url)
    return url_list

def main():
    html = 'http://www.uuzdaisuki.com/'
    dic = open(r"C:\Users\leticia\desktop\dic.txt",'r')
    url_list = []
    real_list = []
    url_list = add_url(html,dic,url_list)
    for url in url_list:
        t = Thread(target = guesshtml,args=(url,real_list))
        t.start()



main()

