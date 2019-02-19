# import threading
# import time
#
# """重新定义带返回值的线程类"""
#
#
# class MyThread(threading.Thread):
#     #func 应该是指针函数
#     def __init__(self, func, args=()):
#         super(MyThread, self).__init__()
#         self.func = func
#         self.args = args
#
#     def run(self):
#         self.result = self.func(*self.args)
#
#     def get_result(self):
#         try:
#             return self.result
#         except Exception:
#             return None
#
#
# """测试函数，计算两个数之和"""
#
#
# def fun(a, b):
#     time.sleep(1)
#     return a + b
#
#
# li = []
# for i in range(4):
#     t = MyThread(fun, args=(i, i + 1))
#     li.append(t)
#     t.start()
# for t in li:
#     t.join()  # 一定要join，不然主线程比子线程跑的快，会拿不到结果
#     print(t.get_result())
#---------------------------------------------------------------------------------------------------
import random
def func2(m, results, index):
    for i in range(2):
        results[index].append(random.choice([0,1,2,3,4,5]))

from threading import Thread
def test4():
    threads = [None] * 4
    results = [[] for i in range(4)]
    print(len(results))
    for i in range(4):
        threads[i] = Thread(target=func2, args=(2500000, results, i))
        threads[i].start() # 开始线程
    for i in range(4):
        threads[i].join()  # 等待线程结束后退出
    return results
print(test4())