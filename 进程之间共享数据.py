import multiprocessing
import time
import os
def func(num):
    print(os.getpid(),"aaaa",num.value)
    num.value=10.78
    time.sleep(5)#子进程改进数值得值，主进程跟着改变
    #现在就出现了进程
def func_1(num):
        num.value = 10.12
        print(os.getpid(),"bbb", num.value)

        time.sleep(5)  # 子进程改进数值得值，主进程跟着改变
if __name__=="__main__":
    start = time.time()
    num_one=multiprocessing.Value("d",10.0)
    print("aaa",num_one.value)
    p=multiprocessing.Process(target=func,args=(num_one,))
    p1=multiprocessing.Process(target=func_1,args=(num_one,))
    p.start()
    #p.join()
    p1.start()
    #p1.join()
    print(num_one.value)
    end = time.time()
    running_time = end - start
    print(running_time)
#import multiprocessing


# def func(num):
#     num.value = 10.78  # 子进程改变数值的值，主进程跟着改变
#
#
# if __name__ == "__main__":
#     num = multiprocessing.Value("d", 10.0)  # d表示数值,主进程与子进程共享这个value。（主进程与子进程都是用的同一个value）
#     print(num.value)
#
#     p = multiprocessing.Process(target=func, args=(num,))
#     p.start()
#     p.join()
#
#     print(num.value)
