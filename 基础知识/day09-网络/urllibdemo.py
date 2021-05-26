#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.request
import ssl
import requests
def test1():
    ssl._create_default_https_context = ssl._create_unverified_context
    myURL = urllib.request.urlopen("https://www.sina.com.cn/")
    print("status:", myURL.getcode())
    data = myURL.read()
    for k, v in myURL.getheaders():
        print('%s: %s' % (k, v))


def test2():
    ssl._create_default_https_context = ssl._create_unverified_context
    myURL = urllib.request.urlopen("https://www.sina.com.cn/")

    f = open("/Users/yunna/Desktop/test.html", "wb")
    content = myURL.read()  # 读取网页内容
    f.write(content)
    f.close()


def test3():
    ssl._create_default_https_context = ssl._create_unverified_context
    encode_url = urllib.request.quote("https://www.runoob.com/")  # 编码
    print(encode_url)

    unencode_url = urllib.request.unquote(encode_url)  # 解码
    print(unencode_url)

def test4():
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        }
        url = "https://www.jianshu.com/p/dd412147e4aa"
        request = urllib.request.Request(url, headers=header)
        reponse = urllib.request.urlopen(request).read().decode("utf-8")
        print(reponse)
    except ValueError:
        print("错误")


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


if __name__ == '__main__':
    test6()










