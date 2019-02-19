import requests
import json
import array
import time
s = requests.session()
url="https://api.17ce.com/ping"
headers_1 = {
    'Host':'https://api.17ce.com',
    'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',


}

data={'user': 'xxx@163.com', 'code': 'xxx','url':'baidu.com',
      'isp':'1,2,3','num':'6','pingcount':30,'pingsize':30}

r=s.post(url=url, headers=headers_1,data=data).text
print(r)
print(int(time.time()))