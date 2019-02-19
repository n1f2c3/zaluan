import sys
import requests
import threading
def scanning(url):
  f=open('a.txt','r')
  for line in f.readlines():
      pad=line.strip()
      urls = url+pad+'/'
      head={
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
      }
      res=requests.request('GET',urls,headers=head).status_code
      if res != 404:
          print(urls)
          scanning(urls)
def thread(url):
    thread1 = threading.Thread(target=scanning,args=(url,));
    thread1.start()
if __name__ == '__main__':
    print('需要加http://和最后的/，例如:http://127.0.0.1/dvwa/')
    url = input('请输入扫描地址：')
    print('开始扫描！！！')
    thread(url)