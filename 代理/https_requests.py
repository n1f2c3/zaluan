#
# custom
# HTTPS
# opener, banner
# 's oracle 10g server supports SSLv3 only
#   https出问题了
import http.client,ssl, urllib.request, socket


class HTTPSConnectionV3(http.client.HTTPSConnection):
    def __init__(self, *args, **kwargs):
        http.client.HTTPSConnection.__init__(self, *args, **kwargs)

    def connect(self):
        sock = socket.create_connection((self.host, self.port), self.timeout)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        try:
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file,
                                        ssl_version=ssl.PROTOCOL_SSLv3)
        except ssl.SSLError as e:
                print("TryingSSLv3.")
        self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file,ssl_version=ssl.PROTOCOL_SSLv23)


class HTTPSHandlerV3(urllib.request.HTTPSHandler):
    def https_open(self,req):
        return self.do_open(HTTPSConnectionV3,req)
    #


# installopener
urllib.request.install_opener(urllib.request.build_opener(HTTPSHandlerV3()))

if __name__ == "__main__":
    r = urllib.request.urlopen("https://baidu.com")
    print(r.read())
