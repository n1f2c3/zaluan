# coding:utf-8
import time

from threading import Thread


def foo(number):
    time.sleep(20)
    return number


class MyThread(Thread):

    def __init__(self, number):
        Thread.__init__(self)
        self.number = number

    def run(self):
        self.result = foo(self.number)

    def get_result(self):
        return self.result


thd1 = MyThread(3)
thd2 = MyThread(5)
thd1.start()
thd2.start()
thd1.join()
thd2.join()

print(thd1.get_result())
print(thd2.get_result())