import optparse
from socket import *
def connScan (tgtHost,tgtPort):
    try:
        connSkt=socket(AF_INET,SOCK_STREAM)
