import requests
import multiprocessing
from multiprocessing import Process, Manager
import linecache
thefile = open("zidian.txt", 'rb')
file_two=r"zidian.txt"
#在windows上读取了文件得二进制到内存中，文件不大，可以承受，必须以RB打开，百度所得
#根据'/n'获取文件有多少行
def getline(thefile_one):
    count = 0
    while True:
        buffer = thefile_one.read(8192*1024)
        if not buffer:
            break
           # python3中，byte字符串就是ansi字符串。str是unicode字符串。所以写文件的时候需要注意文件编码格式
        count += buffer.count(b'\n')
        #print(buffer.count(b'\n'))
        #type(buffer.count(b'\n'))
    thefile_one.close()
    return count;
def request_demo_demo(url,str_one):
    str_two=requests.get(url=url+str_one);
    return "sucess";

#将行数分成5段存到列表中，每段代表每个进程读取文件得行数，我只能写死进程得个数
#有太大得局限性
def request_demo(thefile_one,file_two,count,url,return_back,i):

    c=count//4;
    a=[];
    a[0]=0;
    a[1]=c;
    a[2]=c*2;
    a[3]=c*3;
    a[4]=count-a[3];
    if i==1:
        line_1=[];
        x = a[0]
        y=a[1]
        for i in range(x,y,1):
            count = linecache.getline(file_two, i)
            line_1[i] = count.strip('\n')
            if request_demo_demo(url,line_1[i])=="sucess":
                    #return_back.add(line_1[i]);
                    return_back.add(i)
            return return_back;
    if i==2:
        line_1=[];
        x = a[1]
        y=a[2]
        for i in range(x,y,1):
            count = linecache.getline(file_two, i)
            line_1[i] = count.strip('\n')
            if request_demo_demo(url,line_1[i])=="sucess":
                    #return_back.add(line_1[i]);
                    return_back.add(i)
            return return_back;
        if i == 3:
            line_1 = [];
            x = a[2]
            y = a[3]
            for i in range(x, y, 1):
                count = linecache.getline(file_two, i)
                line_1[i] = count.strip('\n')
                if request_demo_demo(url, line_1[i]) == "sucess":

                    #return_back.add(line_1[i]);
                    return_back.add(i)
                return return_back;
        if i == 4:
                line_1 = [];
                x = a[3]
                y = a[4]
                for i in range(x, y, 1):
                    count = linecache.getline(file_two, i)
                    line_1[i] = count.strip('\n')
                    if request_demo_demo(url, line_1[i]) == "sucess":
                        #return_back.add(line_1[i]);
                        return_back.add(i)
                    return return_back;







def duojincheng():
    #pool=multiprocessing.Pool(processes = 3)
    manager = Manager()
    return_back = manager.dict()

    jobs=set();
    count=getline(thefile)
    for i in range(4):
        p = multiprocessing.Process(target=request_demo, args=(thefile,file_two,count,"http://baidu.com",return_back,i))
        jobs.append(p)
        p.start()
    for proc in jobs:
        proc.join()
    print(return_back);
duojincheng();
