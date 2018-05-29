import requests
url = "http://m.ip138.com/ip.asp?ip="
ipaddr=input("ip:")
try:
    r=requests.get(url+ipaddr)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[-500:])
except:
    print("error")