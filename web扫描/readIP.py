## 提取fofa等信息收集软件扫描结果中的ip，并去重写入txt

## 正则对ip仅做简单判断，如需精确匹配ip地址需要更换pattern中正则表达式

import re

result = []
clean_result = []


def readIPFromFile():
    f = open(r'./out_2020_08_06_14_41_23.csv', 'r')
    pattern = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
    print ("read IP from ",f.name)
    for line in f.readlines():
        ip = pattern.findall(line)
        if not ip == []:
            print (ip[0])
            result.append(ip[0])

def writeIPToFile():
    toFile = open(r'./result_IP.txt', 'w')
    for line in clean_result:
        toFile.write(line+'\n')

def removeSameIP():
    for ip in result:
        if ip not in clean_result:
            clean_result.append(ip)

def main():
    readIPFromFile()
    removeSameIP()
    writeIPToFile()

main()
