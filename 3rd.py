import ooptparse
parser=optparse.OptionParser('usage %prog -H'+'<target host> -p <target port>')
parser.add_option('-R',dest='tgtHost',type='string',help='specify target host')
