from threading import Thread
from threading import Lock

# global_num = 0
# # #
# # #
# # # def func1():
# # #     global global_num
# # #     for i in range(1000000):
# # #         global_num += 1
# # #     print('---------func1:global_num=%s--------' % global_num)
# # #
# # #
# # # def func2():
# # #     global global_num
# # #     for i in range(1000000):
# # #         global_num += 1
# # #     print('--------fun2:global_num=%s' % global_num)
# # #
# # #
# # # print('global_num=%s' % global_num)
# # #
# # # # lock = Lock()
# # #
# # # t1 = Thread(target=func1)
# # # t1.start()
# # #
# # # t2 = Thread(target=func2)
# # # t2.start()






from time import ctime ,sleep
import Thread,threading
loops=[4,2]

class Mythread(threading.Thread):

 def __init__(self,func,args,name):
       threading.Thread.__init__(self)
       self.func=func
       self.args=args
       self.name=name

 def run(self):
       apply(self.func,self.args)

def loop(nloop,nsec):
    print ('start loop',nloop,' at:',ctime())
    sleep(nsec)
    print ('loop',nloop,' done at',ctime())

def main():
    print ('start at',ctime())
    threads=[]
    nloops=range(len(loops))
    for i in nloops:
        t=Mythread(loop,(i,loops[i]),loop.name)
    threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print( 'all done at',ctime())

if __name__ == '__main__':
    main()