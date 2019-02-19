import requests

url='www.wepcc.com/check-ping.html'

header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
'Accept': '*/*',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'https://www.wepcc.com/',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest',
}


#cookie={'sessionid':'8x64ylrinu8b6d6fgp8pjqjtwkkwpvj1'}

data={'node':'3','host':'baidu.com'}

r=requests.post(url=url,data=data,headers=header).text
print (r);