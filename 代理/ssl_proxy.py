import socket

import time

import threading

BUFSIZE = 1024

# https://blog.csdn.net/plain1213/article/details/79457217
class Access_to_Host(object):

    def handler(self, conn, addr):

        self.conn = conn

        self.addr = addr
        # 从数据流中分理对http和https进行处理...返回的值ssl——flag标志位进行区分
        all_src_data, hostname, port, ssl_flag = self.get_dst_host_from_header(self.conn, self.addr)
        #标记1
        #擦得类，新建套接字，此处是如果ssl_flag为true则返回ssl发送得数据，如果不是，则发送httpdata,返回服务器得数据
        all_dst_data = self.get_data_from_host(hostname, port, all_src_data, ssl_flag)
        # if 1 and not 0:
        #         #     print("aaa")
        #         # else:
        #         #     print("bbb")
        # 经过测试 all_dst_data为true和ssl_flag为false时会走入if内
        if all_dst_data and not ssl_flag:

            # self.send_data_to_client(self.conn,all_dst_data)
            # conn_dst是在self.get_data_from_host(hostname, port, all_src_data, ssl_flag)新建的套接字
            self.ssl_client_server_client(self.conn, self.conn_dst, all_dst_data)

        elif ssl_flag:

            sample_data_to_client = b"HTTP/1.0 200 Connection Established\r\n\r\n"

            # print("\nSSL_Flag-1")

            # self.send_data_to_client(self.conn,all_dst_data)

            # print("SSL_Flag-2")

            self.ssl_client_server_client(self.conn, self.conn_dst, sample_data_to_client)

            # print("\nSSL_Flag-3")

        else:

            print('pls check network. cannot get hostname:' + hostname)

        # self.conn.close()

    def ssl_client_server(self, src_conn, dst_conn):

        self.src_conn = src_conn

        self.dst_conn = dst_conn

        while True:

            ###get data from client

            try:

                ssl_client_data = self.src_conn.recv(BUFSIZE)

            except Exception as e:

                print("client disconnct ")

                print(e)

                self.src_conn.close()

                # self.dst_conn.close()

                return False

            if ssl_client_data:

                #####send data to server

                try:

                    self.dst_conn.sendall(ssl_client_data)

                except Exception as e:

                    print("server disconnct Err")

                    self.dst_conn.close()

                    return False

            else:

                self.src_conn.close()

                return False

    def ssl_server_client(self, src_conn, dst_conn):

        self.src_conn = src_conn

        self.dst_conn = dst_conn

        while True:

            ###get data from server

            try:

                ssl_server_data = self.dst_conn.recv(BUFSIZE)

            except Exception as e:

                print("server disconnct ")

                self.dst_conn.close()

                return False

            if ssl_server_data:

                #####send data to client

                try:

                    self.src_conn.sendall(ssl_server_data)

                except Exception as e:

                    print("Client disconnct Err")

                    self.src_conn.close()

                    return False

            else:

                self.dst_conn.close()

                return False

    def ssl_client_server_client(self, src_conn, dst_conn, all_dst_data):
        # conn, addr = self.s_s.accept()
        # 接受连接。套接字必须绑定到地址并侦听连接。返回值是一对 (conn, address)，
        # 其中 conn 是可用于在连接上发送和接收数据的 new 套接字对象，address 是
        # 绑定到连接另一端的套接字的地址。
        self.src_conn = src_conn
        #conn_dst是在self.get_data_from_host(hostname, port, all_src_data, ssl_flag)新建的套接字
        self.dst_conn = dst_conn

        try:

            print("ssl_client_server_client  %s" % all_dst_data)
            # 发送数据
            self.src_conn.sendall(all_dst_data)

        except Exception as e:

            print(e)

            print("cannot sent data(HTTP/1.0 200) to SSL client")

            return False

        threadlist = []

        t1 = threading.Thread(target=self.ssl_client_server, args=(self.src_conn, self.dst_conn))

        t2 = threading.Thread(target=self.ssl_server_client, args=(self.src_conn, self.dst_conn))

        threadlist.append(t1)

        threadlist.append(t2)

        for t in threadlist:
            t.start()

        # t.join()

        ######线程控制,等待线程结束后,远程主机关闭socket后，客户端到主机的socket也不需要再做任何操作了。

        while not self.dst_conn._closed:
            time.sleep(1)

        self.src_conn.close()

    def get_src_client(self):

        self.src_ip = self.s_src.getpeername()

        return self.src_ip

    def send_data_to_client(self, conn_src, data):

        self.conn_src = conn_src

        try:

            self.conn_src.sendall(data)

        except Exception as e:

            print(e)

            print("cannot sent data to client")

            return False

        # self.conn_dst.close()
    # 对http和https的处理
    def get_dst_host_from_header(self, conn_sock, addr):

        self.s_src = conn_sock

        self.addr = addr

        header = ""

        ssl_flag = False

        while True:

            # print("Loop Loop Loop")
            # 从套接字接收数据。返回值是表示接收到的数据的字节对象
            header = self.s_src.recv(BUFSIZE)
            # print("header --- %s"% header)
            if header:

                #####header的一行含有CONNECT，即为SSL（HTTPS）
                # print("----header.......%s  /r/n" % header)
                indexssl = header.split(b"\n")[0].find(b"CONNECT")

                # print("indexsll:"+str(indexssl)+"/r/n----")
                # 如果为ssl链接则进入下面返回ssl_flag=true
                if indexssl > -1:
                    #####CONNECT===7  +8 前面一个空格
                    # print("if--indexssl %s /r/n" % indexssl)
                    hostname = str(header.split(b"\n")[0].split(b":")[0].decode())

                    hostname = hostname[indexssl + 8:]

                    print("hostname  ----%s  /r/n ---"% hostname)
                    port = 443
                    print(port)
                    ssl_flag = True

                    return header, hostname, port, ssl_flag
                # 如果不是ssl链接从http应用协议种header头种寻找host  GET  POST 方法 没有PUT 请求
                # find是查找得第一次出现得字符在第几位
                index1 = header.find(b"Host:")

                index2 = header.find(b"GET http")

                index3 = header.find(b"POST http")
                # 这一段if是将host从http头中抽取出来
                if index1 > -1:
                    # 如果找到HOST
                    # 查找在第几行
                    indexofn = header.find(b"\n", index1)

                    ##host:===5
                    # 将host提取出来
                    host = header[index1 + 5:indexofn]

                elif index2 > -1 or index3 > -1:

                    ###no host sample :'GET http://saxn.sina.com.cn/mfp/view?......

                    host = header.split(b"/")[2]

                else:

                    print("src socket host:")

                    print(self.s_src.getpeername())

                    print("cannot find out host!!:" + repr(header))

                    return

                break
        # 对抽取出来得host头进行decode处理去掉回车
        host = str(host.decode().strip("\r").lstrip())
        # 下面是从头中抽取port，如果没有port则默认得是80
        if len(host.split(":")) == 2:

            port = host.split(":")[1]

            hostname = host.split(":")[0].strip("")

        else:

            port = 80

            hostname = host.split(":")[0].strip("")
        # 设定ssl_flag为false
        ssl_flag = False

        return header, hostname, int(port), ssl_flag

    def get_data_from_host(self, host, port, sdata, ssl_flag):
        # 新建socket连接
        self.conn_dst = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 初始化数据
        all_dst_data = ""

        try:
            # 尝试建立连接
            self.conn_dst.connect((str(host), port))

        except Exception as e:
            # 处理异常
            print(e)

            print("get_data_from_host: cannot get host:" + host)

            self.conn_dst.close()

            return False

        # con_string="("+server+","+port+")"

        ############https只建立链接

        try:

            if ssl_flag:
                # 如果是ssl_flag则返回数据
                return all_dst_data

            else:
                # 如果是htp 则发送http的应用层的数据包
                self.conn_dst.sendall(sdata)

        except Exception as e:

            print(e)

            print("cannot send data to host:" + host)

            self.conn_dst.close()

            return False

        # buffer=[]
        # 等待数据的接受
        rc_data = self.conn_dst.recv(BUFSIZE)

        #####剩下的data交给线程去获取

        return rc_data


class Server(object):

    def Handle_Rec(conn_socket, addr):

        print("This is Handler Fun")

        pass

    def __init__(self, host, port):

        print("Server starting......")

        self.host = host

        self.port = port
        # IPV4得协议
        self.s_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 第二个参数SO_REUSEADDR可以用在以下四种情况下： (摘自《Unix网络编程》卷一，即UNPv1)
        #      1、当有一个有相同本地地址和端口的socket1处于TIME_WAIT状态时，而你启动的程序的socket2要占用该地址和端口，你的程序就要用到该选项。
        #      2、SO_REUSEADDR允许同一port上启动同一服务器的多个实例(多个进程)。但每个实例绑定的IP地址是不能相同的。在有多块网卡或用IP Alias技术的机器可
        # 以测试这种情况。
        #      3、SO_REUSEADDR允许单个进程绑定相同的端口到多个socket上，但每个socket绑定的ip地址不同。这和2很相似，区别请看UNPv1。
        #      4、SO_REUSEADDR允许完全相同的地址和端口的重复绑定。但这只用于UDP的多播，不用于TCP。
        #第一个参数要在套接字级别上设置选项  必须讲level设置为SSOL_SOCKET
        #看不懂得函数
        self.s_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 将套接字绑定到 address。套接字不必已绑定
        self.s_s.bind((host, port))
        #设置监听链接得个数
        self.s_s.listen(20)

    def start(self):

        while True:

            try:
                # 接受连接。套接字必须绑定到地址并侦听连接。返回值是一对 (conn, address)，
                # 其中 conn 是可用于在连接上发送和接收数据的 new 套接字对象，address 是
                # 绑定到连接另一端的套接字的地址。
                #
                conn, addr = self.s_s.accept()
                print(conn)
                print(addr)
                # 走到这里开启线程调用了Access_to_Host().handler  参数conn addr
                threading.Thread(target=Access_to_Host().handler, args=(conn, addr)).start()
                # Access_to_Host.handler(conn,addr)
            except Exception  as e:

                print(str(e))

                print("\nExcept happend")


if __name__ == "__main__":
    svr = Server("127.0.0.1", 8080)

    svr.start()
