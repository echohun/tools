#! -*- encoding:utf-8 -*-
# python3


import requests

def guesshtml(url_list,real_list):
    for url in url_list:
        try:
            r = requests.get(url, timeout=3)
        except:
            r.status_code=404
        if r.status_code==200:
            print("存在: "+url)
            real_list.append(url)
        else:
            print("不存在: %s 错误代码: %d"% (url,r.status_code))
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
    real_list = guesshtml(url_list,real_list)

main()