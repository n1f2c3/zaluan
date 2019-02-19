# -*- coding: GBK -*-
from  multiprocessing import Process,Pool
import linecache
import time
file_one=open("a.txt","rb");
count = linecache.getline(filename,linenum)
def gethansghu():
    count=0;
    thefile=open("a.txt","rb")
    while True:
        buffer=thefile.read(8192*1024)
        if not buffer:
            break
        count +=buffer.count('\n')
    thefile.close()