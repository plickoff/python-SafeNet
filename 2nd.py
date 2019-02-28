import zipfileimport optparse
from threading import Thread
def extractFile(zFile,password):
    try:
        zFIle.extractall(pwd=password)
        print '[+] found password' + password +'\n'
    except:
        pass
def main():
    parser=opotparse.OptionParser("usage%prog"+"-f <zipfile> -d <dictionary>")
    parser.add_option('-f',dest='zname',type='string',help='specify zip file')
    parser.add_option('-d',dest='zname',type='string',help='specify dictionary file')
    (option,args)=parser.parse_args()
    if (option.zname==none) | (options.dname ==None):
        print parser.usage
        exit()
    else:
        zname= options.zname
        dname=options.dname
        zFile=zipfile.ZipFIle(zname)
        passFile=open(dname)
        for line in passFIle.readlines():
            password=line.strip('\n')
            t= Thread(target=extractFile,args=(zFile,password))
            t.start()
if __name__="__main__":
    main()
