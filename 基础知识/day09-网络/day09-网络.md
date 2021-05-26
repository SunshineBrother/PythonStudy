# day09-网络
 
Python urllib 库用于操作网页 URL，并对网页的内容进行抓取处理。

**urllib 包 包含以下几个模块：**
- urllib.request - 打开和读取 URL。
- urllib.error - 包含 urllib.request 抛出的异常。
- urllib.parse - 解析 URL。
- urllib.robotparser - 解析 robots.txt 文件。


## urllib.request

urllib.request 定义了一些打开 URL 的函数和类，包含授权验证、重定向、浏览器 cookies等。
urllib.request 可以模拟浏览器的一个请求发起过程。
```
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
```

- url：url 地址。
- data：发送到服务器的其他数据对象，默认为 None。
- timeout：设置访问超时时间。
- cafile 和 capath：cafile 为 CA 证书， capath 为 CA 证书的路径，使用 HTTPS 需要用到。
- cadefault：已经被弃用。
- context：ssl.SSLContext类型，用来指定 SSL 设置。


```
def test1():
    ssl._create_default_https_context = ssl._create_unverified_context
    myURL = urllib.request.urlopen("https://www.sina.com.cn/")
    print("status:", myURL.getcode())
    data = myURL.read()
    for k, v in myURL.getheaders():
        print('%s: %s' % (k, v))
```

打印如下
```
status: 200
Server: Tengine
Content-Type: text/html
Content-Length: 529410
Connection: close
Date: Wed, 26 May 2021 07:51:48 GMT
Vary: Accept-Encoding
ETag: "60adfd32-7c26e"V=5965C31
X-Powered-By: shci_v1.13
Expires: Wed, 26 May 2021 07:52:00 GMT
Cache-Control: max-age=60
X-Via-SSL: ssl.25.sinag1.shx.lb.sinanode.com
Edge-Copy-Time: 1622015482167
Via: https/1.1 ctc.guangzhou.union.119 (ApacheTrafficServer/6.2.1 [cRs f ]), https/1.1 ctc.ningbo.union.46 (ApacheTrafficServer/6.2.1 [cRs f ]), cache28.l2cn2656[0,0,200-0,H], cache32.l2cn2656[1,0], cache8.cn1997[11,10,200-0,M], cache8.cn1997[13,0]
X-Via-Edge: 16220155086479d8cec728b8388b740aabd5a
X-Via-CDN: f=alicdn,s=cache8.cn1997,c=180.164.237.82;f=edge,s=ctc.ningbo.union.47.nb.sinaedge.com,c=114.236.140.157;f=Edge,s=ctc.ningbo.union.46,c=115.238.190.47
Ali-Swift-Global-Savetime: 1622015508
Age: 46
X-Cache: MISS TCP_REFRESH_MISS dirn:-2:-2
X-Swift-SaveTime: Wed, 26 May 2021 07:52:34 GMT
X-Swift-CacheTime: 14
Timing-Allow-Origin: *
EagleId: b4a37a1c16220155539972809e
```

**read**
read() 是读取整个网页内容,如果要将抓取的网页保持到本地，可以使用write() 方法 函数：

```
def test2():
    ssl._create_default_https_context = ssl._create_unverified_context
    myURL = urllib.request.urlopen("https://www.sina.com.cn/")
    print("status:", myURL.getcode())

    f = open("/Users/yunna/Desktop/test.html", "wb")
    content = myURL.read()  # 读取网页内容
    f.write(content) #已写入二进制的方式创建文件
    f.close()
```


### 编码与解码

URL 的编码与解码可以使用 urllib.request.quote() 与 urllib.request.unquote() 方法：
```
def test3():
    ssl._create_default_https_context = ssl._create_unverified_context
    encode_url = urllib.request.quote("https://www.runoob.com/")  # 编码
    print(encode_url)

    unencode_url = urllib.request.unquote(encode_url)  # 解码
    print(unencode_url)


打印
https%3A//www.runoob.com/
https://www.runoob.com/
```


### 模拟头部信息

我们抓取网页一般需要对 headers（网页头信息）进行模拟，这时候需要使用到 urllib.request.Request 类：

```
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
```
- url：url 地址。
- data：发送到服务器的其他数据对象，默认为 None。
- headers：HTTP 请求的头部信息，字典格式。
- origin_req_host：请求的主机地址，IP 或域名。
- unverifiable：很少用整个参数，用于设置网页是否需要验证，默认是False。。
- method：请求方法， 如 GET、POST、DELETE、PUT等。


譬如我们随便打开一个简书的网页
```
ssl._create_default_https_context = ssl._create_unverified_context
myURL = urllib.request.urlopen("https://www.jianshu.com/p/dd412147e4aa")

```

会报出`urllib.error.HTTPError: HTTP Error 403: Forbidden`的错误

产生原因： 
之所以出现上面的异常,是因为如果用 urllib.request.urlopen 方式打开一个URL,服务器端只会收到一个单纯的对于该页面访问的请求,但是服务器并不知道发送这个请求使用的浏览器,操作系统,硬件平台等信息,而缺失这些信息的请求往往都是非正常的访问,例如爬虫.有些网站为了防止这种非正常的访问,会验证请求信息中的UserAgent(它的信息包括硬件平台、系统软件、应用软件和用户个人偏好),如果UserAgent存在异常或者是不存在,那么这次请求将会被拒绝(如上错误信息所示)所以可以尝试在请求中加入UserAgent的信息

```
def test4():
    ssl._create_default_https_context = ssl._create_unverified_context
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    url = "https://www.jianshu.com/p/dd412147e4aa"
    request = urllib.request.Request(url,headers=header)
    reponse = urllib.request.urlopen(request).read()
    print(reponse)
```


**代理服务器设置**

现在我们已经学会了伪装成浏览器去抓取网页，那么如果遇到更厉害的反扒手段，发现某一个IP频繁访问网址，会被服务器屏蔽，那么该怎么办呢？这是就需要代理服务器上场了。

首先代理服务器在百度上搜索一下，有很多，我们随便点进去一个：

![](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day09-网络/代理服务器设置.png)

我们选取第一个：116.214.32.51   8080即IP：端口号

接下来，我们上述代码可以修改成如下：

```
def test5():
    ssl._create_default_https_context = ssl._create_unverified_context
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    proxies = {'http': '116.214.32.51:8080',
               'http': '117.121.100.9:3128'}

    url = "https://www.jianshu.com/p/dd412147e4aa"
    req = urllib.request.Request(url, headers=header)
    # 设置代理服务器信息
    handler = urllib.request.ProxyHandler(proxies)
    # 2.使用上面创建的的 handler 构建一个 opener
    opener = urllib.request.build_opener(handler)

    response = opener.open(req)
    # 获取服务器响应内容
    html = response.read().decode("utf-8")
    print(html)
```


### Post请求

网站登录和注册等功能一般都是通过post请求方式做的，学会用Requests发起post请求也是爬取需要登录网站的第一步。

```
def test6():
    # 测试请求地址
    req_url = "https://httpbin.org/post"
    # 表单数据
    formdata = {
        'username': 'test',
        'password': '123456',
    }
    # 添加请求头
    req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    # 发起请求
    response = requests.post(
        req_url,
        data=formdata,
        headers=req_header
    )
    print(response.text)
    # 如果是json文件可以直接显示
    # print (response.json())

```



## 其他概念

如果你真以为Requests网络请求库只有Get请求和Post请求，那就大错特错了。它还一些其他用法，也是爬虫经常需要的，我们一起来看看吧。


### Auth验证

不知道小伙伴配置过刚买的路由器没有，刚配置的要进入后台一般都需要浏览器的Auth验证，需要输入用户名和密码，它的原理就是将用户名:密码base64加密后放在http的请求头部，然后发送给后台进行验证。我们的Requests也必然支持这种操作，不过用的相对较少。
 
```
import requests

auth=('admin', 'admin')

response = requests.get(
    'http://192.168.1.1', 
    auth = auth
)
print (response.text)


```

### 代理

使用http或https代理，可能是我们解决反爬比较重要的一个环节


当我们的IP被封时，我们往往会采用代理。相当于我喜欢一个女孩，但是她把我拉入黑名单了，这个时候往往会找她的闺蜜进行操作，我要把对女孩说的话跟她闺蜜说，然后让闺蜜转交给她。闺蜜在把她对我说的话返回给我。如果这个闺蜜也被她拉入黑名单，我们在换一个她的闺蜜。理论上一般我们都会采用闺蜜池，也就是我们所说的IP代理池。需要钱呀！！！！

```
import requests

# 根据协议类型，选择不同的代理
proxies = {
    "http": "http://12.34.56.79:9527",
    "https": "http://12.34.56.79:9527",
}

response = requests.get(
    "http://www.baidu.com", 
    proxies = proxies
)
print(response.text)


```
 
### Cookies

使用python的requests开发爬虫类程序时，经常需要将之前请求返回的set-cookie值，作为下一个请求的cookie发送。比如模拟登录之后的返回的sessionId，就需要作为后续请求的cookie参数。

```
import requests

response = requests.get("http://www.baidu.com/")

# 返回CookieJar对象:
cookiejar = response.cookies

#打印cookiejar
print (cookiejar)

#下一次访问带上 上一次的cookies
response = requests.get("http://www.baidu.com/", cookies=cookie_jar)

#打印响应内容
print (response.text)


```

### Session


在 requests里，session是一个比较强大的对象，这个对象代表一次用户会话：从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开，
会话能让我们在跨请求时候保持某些参数。比如在同一个 Session 实例发出的所有请求之间保持 cookie 。
```
import requests

# 创建session对象，可以保存Cookie值
session = requests.session()

# 添加请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

# post参数
data = {
    "email":"xxxx",
    "password":"xxxx"
}

# 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在session里
session.post(
    "http://www.jikedaohang.com/login",
    data = data
)

# session包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面。
# 比如个人中心页面
response = session.get(
    "http://www.jikedaohang.com/1562336754/profile"
)

#  打印响应内容
print (response.text)


```
 
### 处理HTTPS请求(SSL证书验证)

在想处理这块知识点，我们需要了解一些东西：

- SSL：安全套接字层。是为了解决HTTP协议是明文，避免传输的数据被窃取，篡改，劫持等。
- TSL：Transport Layer Security，传输层安全协议。TSL其实是SSL标准化后的产物，即SSL／TSL
- HTTPS在传输数据时，会先建立TCP连接，建立起TCP连接后，会建立TSL连接。
- 请求可以为HTTPS请求验证SSL证书，就像web浏览器一样，SSL验证默认是开启的，

如果证书验证失败，请求会抛出SSLError:
 
```
SSLError: ("bad handshake: Error([('SSL routines', 'ssl3_get_server_certificate', 'certificate verify failed')],)",)

```

遇到请求的SSL验证，可以直接跳过不验证，将verify=False设置一下即可。

```
 import requests
response = requests.get("https://www.12306.cn/mormhweb/", verify = False)
print (response.text)

```

如果验证，那么verify参数可以是传入CA_BUNDLE文件的路径或传入包含可信任CA证书的文件夹路径
```
import requests
response = requests.get("https://www.12306.cn/mormhweb/", verify = './certfile')
print (response.text)


```
结果： 1.HTTPS请求进行SSL验证或忽略SSL验证才能请求成功，忽略方式为verify=False。

2.SSL证书是由CA机构颁发的，是需要花钱的。








