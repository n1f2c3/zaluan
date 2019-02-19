import requests
import linecache
def request_demo_demo(url, line_1):
     headers={  "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36" }

     r=requests.get(url=url+line_1,headers=headers)
    # r.status_code == requests.codes.ok
     return  r.status_code
if __name__=="__main__":
    print("aa")
    file_write=open("saomiaohoudemulu.txt","a+")
    count=0;
    thefile=open("zidian.txt","rb")
    filename=r"a.txt"
    while True:
        buffer=thefile.read(8192*1024)
        if not buffer:
            break
        count +=buffer.count(b'\n')
    thefile.close()
    line_1=[];

    count_one=''
    for i in range(1,count+1):
        count_one = linecache.getline(filename, i)
        count_one=count_one.strip('\n')
        line_1.append(count_one)
        z=request_demo_demo("https://baidu.com/", line_1[i-1])
        if z == 200 :
            file_write.write(line_1[i-1]+'\n')
    file_write.close();
    with open("saomiaohoudemulu.txt","r") as  f:
         for line in f.readlines():
             print(line.split()[0])








