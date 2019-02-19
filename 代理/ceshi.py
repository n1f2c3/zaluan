
header="""GET / HTTP/1.1
Host: push.services.mozilla.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Sec-WebSocket-Version: 13
Origin: wss://push.services.mozilla.com/
Sec-WebSocket-Protocol: push-notification
Sec-WebSocket-Key: QoFv31UeQd89qsoekuQ8iA==
Connection: keep-alive, Upgrade
Pragma: no-cache
Cache-Control: no-cache
Upgrade: websocket
"""


if False and not True:
    print("aaa")
else:
    print("bbb")

# host = header.split("/")[2]
# print(host)
# index1 = header.find("Host:")

# if index1 > -1:
#     # 如果找到HOST
#     # 查找在第几行
#     indexofn = header.find("\n", index1)
#     print("%d /r/n " % index1)
#
#     print("%s /r/n "% indexofn)
#     ##host:===5
#
#     host = header[index1 + 5:indexofn]
#     print(host)