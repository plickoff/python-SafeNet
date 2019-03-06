import optparse
from socket import *
def connScan (tgtHost,tgtPort):
    try:
        connSkt=socket(AF_INET,SOCK_STREAM)
        connSkt=connect((tgtHost,tgtPort))
        print '[+]%d/tcp open' % tgtPort
        connSkt.close()
