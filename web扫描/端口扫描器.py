#! -*- encoding:utf-8 -*-
# python3

import nmap
import optparse

def nmapScan(tgtHost,tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost,tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print ("[*] "+tgtHost+"tcp/"+tgtPort+" "+state)

def main():
    parse = optparse.OptionParser("usage %prog -H <target host> -P <target port>")
    parse.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    parse.add_option('-P',dest='tgtPort',type='string',help='specify target port')
    (options,args) = parse.parse_args()
    if (options.tgtHost==None):
        print (parse.usage)
    elif (options.tgtPort==None):
        print ('use default port')
        tgtHost = options.tgtHost
        tgtPorts=[20,21,22,23,25,69,80,109,110,139,179,443,445,544,1080,1433,1434,1521,1158,2100,3306,3389,7001,8000,8080,8081,9080,9090]
        for tgtPort in tgtPorts:
            nmapScan(str(tgtHost),str(tgtPort))
    else:
        tgtHost = options.tgtHost
        tgtPorts = str(options.tgtPort).split(',')
        for tgtPort in tgtPorts:
             nmapScan(str(tgtHost),str(tgtPort))

if __name__ =='__main__':
    main()