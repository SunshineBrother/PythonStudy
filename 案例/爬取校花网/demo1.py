#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests
from lxml import etree
import os


class XHSpider():

    def __init__(self):
        # 默认第2页开始
        self.pn = 2
        # 默认URL
        self.url = 'http://www.xiaohuar.com/daxue/index_{0}.html'

        # 目录
        self.dir = '/Users/yunna/Desktop/校花/'

        #刚开始就创建一个目录
        if not os.path.exists(self.dir):  # 如果文件夹不存在
            os.mkdir(self.dir)  # 创建文件夹

        # 添加请求头,模拟浏览器
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

    # 发起请求
    def loadpage(self):

        # 拼接请求地址
        req_url = self.url.format(self.pn)

        print("req_url:",req_url)

        # 发起请求
        reponse = requests.get(url=req_url, headers=self.headers)

        # 取返回的内容
        content = reponse.text

        # 构造xpath解析对象
        html = etree.HTML(content)

        # 先取出这个页面所有div标签
        div_list = html.xpath('//*[@id="wrap"]/div/div')

        for div in div_list:
            # 从从每个div标签取出详情页链接 .代表当前位置
            url = div.xpath('//*[@id="wrap"]/div/div/div[*]/div/div[*]/a/@href')[0]
            desc_url = "http://www.xiaohuar.com" + url
            print("desc_url:", desc_url)
            # 标题
            title = div.xpath('//*[@id="wrap"]/div/div/div[*]/div/a/img/@alt')[0]
            img_title = title.encode('utf-8').decode('utf-8')
            print("img_title:", img_title)
            # 封面图片地址、这个地址好像没用。发现相册里面有这种图片
            img_url = div.xpath('//*[@id="wrap"]/div/div/div[*]/div/a/img/@src')[0]
            print("img_url:", img_url)
            #创建每个校花的文件夹
            folder = self.dir + img_title
            if not os.path.exists(folder):  # 如果文件夹不存在
                os.mkdir(folder)  # 创建文件夹

            self.download(img_url,img_title)
            # #开始请求详情页，把标题传过去，后面有用
            # self.loaddescpage(desc_url, img_title)

    # 详情页
    def loaddescpage(self, desc_url, img_title):
        # 发起请求
        reponse = requests.get(url=desc_url, headers=self.headers)
        # 取返回的内容
        content = reponse.text
        # 构造xpath解析对象
        html = etree.HTML(content)

        # 取出详细资料
        content_p_list = html.xpath('//*[@id="wrap"]/div/div/div[1]/div/div[4]/div[1]/p')
        content = ""
        for p in content_p_list:
            p_text = p.xpath('//*[@id="wrap"]/div/div/div[1]/div/div[4]/div[1]/p[*]/text()')[0]
            content = content + p_text + "\n"
        print(content)

        # 取出图片
        big_imgs = []
        for p in content_p_list:
            p_image = p.xpath('//*[@id="wrap"]/div/div/div[1]/div/div[4]/div[1]/p[*]/img/@src')[0] + ""
            big_imgs.append(p_image)


        # 做图片地址容错处理
        for index in range(len(big_imgs)):
            big_img = big_imgs[index]
            if big_img.startswith('http') or big_img.endswith('.jpg'):
                if big_img.startswith('http'):
                    self.download(big_img, img_title)

    # 图片下载
    def download(self, big_img, img_title):
        print('正在下载:', big_img,img_title)
        # 发起请求
        reponse = requests.get(url=big_img, headers=self.headers)
        # 读取二进制内容
        content = reponse.content
        # 图片地址
        img_dir = self.dir + img_title + "/" + big_img[-15::]
        print("img_dir:",img_dir)

        # 保存到本地
        with open(img_dir, 'wb') as f:
            f.write(content)
            f.close()

if __name__ == "__main__":
    xhs = XHSpider()
    #这正确的逻辑应该自动提取下一页，然后自动加载，不过数据量不大。可以简单通过循环提取。
    for i in range(2, 30):
        print('爬取第%d页' % i)
        xhs.pn = i  # 把每页赋值给pn
        xhs.loadpage()

