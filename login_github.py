#coding=utf8
import re
import socket  
import urllib,urllib2,cookielib

# 设置超时时间
timeout = 20    
socket.setdefaulttimeout(timeout)

# 其它全局变量
host = 'http://github.com'
login_url = 'https://github.com/login'
post_url = 'https://github.com/session'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
username = '填写用户名'
password = '填写密码'

# 构建opener
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

request = urllib2.Request(login_url,headers=headers)
response = opener.open(request)
# 获取token
print '正在获取token……'
token_pattern = re.compile('<input name="authenticity_token" type="hidden" value="(.*?)"',re.S)
token = re.findall(token_pattern,response.read().decode('utf8'))[0]
#print token

# 构造post数据
postdata = urllib.urlencode({
'commit':'Sign in',
#'utf8':'✓',
'utf8':'%E2%9C%93',
'authenticity_token':token,
'login':username,
'password':password
})

# 验证登陆
print '正在登录github……'
request = urllib2.Request(post_url,postdata,headers)
response = opener.open(request)
#print response.read()

print '登陆成功!'
