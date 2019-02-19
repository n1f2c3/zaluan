import requests

s = requests.session()
url="http://www.wepcc.com"
headers_1 = {
    'Host':'www.wepcc.com',
    'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Accept': '*/*',
    "Accept - Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    'Accept - Encoding': 'gzip, deflate',
    'Referer': 'https://www.wepcc.com/',
    'Content - Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    # 'X-Requested-With':'23',
    'Content - Length':'41',
    'DNT': '1',
    'Connection': 'keep-alive'

}


r=s.get(url=url, headers=headers_1)
print(r.headers)
print(r.cookies)
print(r.url)
data={'host': 'baidu.com', 'node': '1,2,3,4,5,6'}
r_1=s.post(url=url, headers=headers_1,data=data).text
# print(r_1)