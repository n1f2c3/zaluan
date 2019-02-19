
import socket
import hashlib
import base64
import string
# def getIP(domain):
#     myaddr = socket.getaddrinfo(domain, 'http')
#     print(myaddr[0][4][0])
# getIP("www.baidu.com")
user='test@17ce.com'
pwd='123456'
t='1532598458'
m=hashlib.md5()
m.update(pwd.encode("utf8"))
c=m.hexdigest()
c1=c[4:19]+str(user)+str(t)
print(type(c1))
z1=base64.b64encode(c1.encode('utf-8'))
print(type(z1))
z2=str(z1,'utf-8');

m=hashlib.md5()
m.update(z2.encode("utf-8"))
z3=m.hexdigest()
print(z3)
# a=hashlib.md5(base64.b64encode(hashlib.md5(pwd)[4,19].trim(user).t))
# print(a)

import hashlib

import sys


def md5s():
    m = hashlib.md5()

    pwd = '123456'

    m.update(pwd.encode("utf8"))

    print(m.hexdigest())


if __name__ == '__main__':
    md5s()
