from concurrent.futures import ProcessPoolExecutor # 进程池模块
from concurrent.futures import ThreadPoolExecutor # 线程池模块
import os, time, random #  下面是以进程池为例, 线程池只是模块改一下即可
def talk(name):
    print('name: %s  pis%s  run' % (name,os.getpid()))
    #time.sleep(random.randint(1, 3))
    time.sleep(100)
if __name__ == '__main__':
        pool = ProcessPoolExecutor(10) # 设置线程池大小,默认等于cpu核数 f
        for i in range(10):
            pool.submit(talk, 'jincheng%s' % i) # 异步提交(只是提交需要运行的线程不等待) # 作用1:关闭进程池入口不能再提交了   作用2:相当于jion 等待进程池全部运行完毕
        pool.shutdown(wait=True)
        print('主进程')


# from concurrent.futures import ProcessPoolExecutor #进程池模块
# import os,time,random
# #1、同步调用:提交完任务后、就原地等待任务执行完毕,拿到结果,再执行下一行代码(导致程序串行执行)
# def talk(name):
#     print('name:%s pisss run' % name,os.getpid())
#     time.sleep(random.randint(1,3))
# if __name__=='__main__':
#     pool=ProcessPoolExecutor(4)
#     for i in range(10):
#         pool.submit(talk,'进程'+str(i)).result()#同步迪奥用,result(),相当于join串行
#     pool.shutdown(wait=True)
#     print('主进程')
#同步？
# from concurrent.futures import ProcessPoolExecutor  # 进程池模块
# import os, time, random
# def talk(name):
#    # print('name: %s  pis%s  run' % name,os.getpid())
#    #无法理解为什么%s左边是空格无法解析
#     print('name:%s pisss run' % name, os.getpid())
#     time.sleep(random.randint(1, 3))
# if __name__ == '__main__':
#     z='1'
#
#     pool = ProcessPoolExecutor(4)
#     for i in range(10):
#         pool.submit(talk, 'jincheng%s' % i)  # 异步调用，不需要等待
#     pool.shutdown(wait=True)
#     print('主进程')
#异步
# import time
# import requests
# from concurrent.futures import ThreadPoolExecutor  # 线程池模块
#
# def get(url):
#     print('GET %s' % (url))
#     response = requests.get(url)  # 下载页面
#     time.sleep(3)  # 模拟网络延时
#     return{'url': url, 'content': response.text}  # 页面地址和页面内容
# def parse(res):
#     res = res.result()
#     print(type(res))# !取到res结果 【回调函数】带参数需要这样
#     #这有毒吧，这语法好奇怪，输出的字典需要用()抱起来其他用,不对默认的应该是需要包起来
#     print('%s res is%s' % (res['url'], len(res['content'])))
# if __name__ == '__main__':
#     urls = {
#         'http://www.baidu.com',
#         'http://www.360.com',
#         'http://www.iqiyi.com'
#     }
#     pool = ThreadPoolExecutor(2)
#     for i in urls:
#         pool.submit(get, i).add_done_callback(parse)  # 【回调函数】执行完线程后，跟一个函数
