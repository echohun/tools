#! -*- encoding:utf-8 -*-
# python3


import requests
from threading import Thread


def guesshtml(url,real_list):
    try:
        r = requests.get(url, timeout=30)
    except:
        print("不存在:  %s" %(url))
    else:
        print("存在:  %s  状态码:  %d" % (url,r.status_code))
        real_list.append(url)
    return real_list

def add_url(html,html2,dic,url_list):
    for line in dic:
        line = line.replace('\n','')
        url = html + line + html2
        url_list.append(url)
    return url_list

def main():
    html = 'http://'
    html2 = '.uuzdaisuki.com/'
    dic = open(r"C:\Users\leticia\desktop\name.txt",'r')
    url_list = []
    real_list = []
    url_list = add_url(html,html2,dic,url_list)
    for url in url_list:
        t = Thread(target = guesshtml,args=(url,real_list))
        t.start()



main()

