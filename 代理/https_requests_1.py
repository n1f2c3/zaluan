#-*-coding:utf-8-*-
# Time:2017/9/25 20:41
# Author:YangYangJun

import requests
import ssl
from requests.auth import HTTPBasicAuth

def post_login():

    url = "https://www.url"
    values = {}
    values['username'] = 'username'
    values['password'] = 'password'
    response = requests.post(url,values)
    print (response.text)



def get_login():
    url = "https://www.url"
    values = {}
    values['username'] = 'username'
    values['password'] = 'password'
    #geturl = url + '?' + values
    response = requests.get(url, values)
    print (response.content)


def post_loginHttps1():

    url = "https://www.url"
    values = {}
    values['username'] = 'username'
    values['password'] = 'password'
    #临时解决https的方法1
    response = requests.post(url,values,verify=False)
    print (response.text)

def post_loginHttps2():
    #解决https方法2
    ssl._create_default_https_context = ssl._create_unverified_context

    url = "https://www.baidu.com"
    values = {}
    values['username'] = 'username'
    values['password'] = 'password'
    #临时解决https的问题
    response = requests.post(url,verify=True)
    print (response.text)



if __name__ == '__main__':
    # post_login()
    #get_login()
    post_loginHttps2()
    # post_loginHttps2()

    #出现下面错误的原因主要是因为打开了fiddler，关闭fiddler即可。

#     raise SSLError(e, request=request)
# requests.exceptions.SSLError: HTTPSConnectionPool(host='www.yiyao.cc', port=443): Max retries exceeded with url: /user/loginWeb (Caused by SSLError(SSLError(1, u'[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:661)'),))
#