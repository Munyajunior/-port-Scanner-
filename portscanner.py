#A simple scanner that will take a given address as input IP
#list ports and will atempt to make a TCP connection towards a port and wait a response(tcp)
#from that response we will know the state of the port  

from socket import *

def conScan(tgtHost, tgtPort):
    try:
        conskt = socket(AF_INET, SOCK_STREAM)
        conskt.connect((tgtHost, tgtPort))
        print('[+]%d/tcp Open'% tgtPort)
        conskt.close()
    except:
        print('[-]%d/tcp Closed'% tgtPort)
        

def portScan(tgtHost,tgtPort):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-] cannot resolve %s'% tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan result of: %s ' % tgtName[0])
    except:
        print('\n[+] Scan result of: %s ' % tgtIP)
    setdefaulttimeout(0.5)
    
 
        
if __name__ == '__main__':
    tgtHost = input("Enter target Ip or Domain")
    for tgtPort in range(1, 1025):
        print('Scanning Port: ' + str(tgtPort))
        conScan(tgtHost, int(tgtPort))
    portScan(tgtHost,tgtPort)