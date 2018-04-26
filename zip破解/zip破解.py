from zipfile import *
from threading import Thread


def extractfile(zfile, password):
    try:
        zfile.extractall(pwd = password)
        print ("[+]"+password)
        return password
    except:
        print ("[-]"+password)
        return

def main():
    zfile = PyZipFile(r"C:\Users\leticia\desktop\233.zip")
    passfile = open(r"C:\Users\leticia\desktop\password.txt",'r')
    for line in passfile.readlines():
        password = line.strip('\n')
        t = Thread(target = extractfile,args=(zfile,password))
        t.start()


main()
