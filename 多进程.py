from threading import Thread
import time


from multiprocessing import Process

file_path = 't'
fd = open(file_path, 'r')


def deal(thread_num):

    i = 1
    line_list = []

    #20是我的文件行数，正式情况下可以通过wc -l t获取
    while i <= 20/thread_num:
        line_list.append(fd.readline())
        i += 1
    return line_list


def todo(thread_name, line_list):
    # print 'thread_name:',thread_name,'start'
    for line in line_list:
        print(str(thread_name) + ' counsume:' + line)
        time.sleep(1000);
    # print 'thread_name:', thread_name, 'end'


if __name__ == '__main__':
    thread_num = 10
    thread_list = []
    for i in range(thread_num):
        line_list = deal(thread_num)
        t = Thread(target=todo, args=[i, line_list])
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

