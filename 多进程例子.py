import multiprocessing
import time

def func(num):
    num.value = 10.78  # 子进程改变数值的值，主进程跟着改变
    time.sleep(1000)

if __name__ == "__main__":
    num = multiprocessing.Value("d", 10.0)  # d表示数值,主进程与子进程共享这个value。（主进程与子进程都是用的同一个value）
    print(num.value)

    p = multiprocessing.Process(target=func, args=(num,))
    p1 = multiprocessing.Process(target=func, args=(num,))
    p.start()
    p1.start()

    print(num.value)