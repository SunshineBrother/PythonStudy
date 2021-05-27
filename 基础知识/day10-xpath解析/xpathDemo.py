#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from lxml import etree
import os

def test1():
    data = """
            <div>
                <ul>
                     <li class="item-0"><a href="link1.html">first item</a></li>
                     <li class="item-1"><a href="link2.html">second item</a></li>
                     <li class="item-inactive"><a href="link3.html">third item</a></li>
                     <li class="item-1" id="1" ><a href="link4.html">fourth item</a></li>
                     <li class="item-0" data="2"><a href="link5.html">fifth item</a>
                 </ul>
             </div>
            """
    # 构造了一个XPath解析对象。etree.HTML模块可以自动修正HTML文本。
    html = etree.HTML(data)

    # 选取ul下面的所有li节点
    li_list = html.xpath('//ul/li')
    print(li_list)
    print("-----------------------------------------")
    # 选取ul下面的所有a节点
    a_list = html.xpath('//ul/li/a')
    print(a_list)
    print("-----------------------------------------")
    # 选取ul下面的所有a节点的属性herf的值
    herf_list = html.xpath('//ul/li/a/@href')
    print(herf_list)
    print("-----------------------------------------")
    # 选取ul下面的所有a节点的值
    text_list = html.xpath('//ul/li/a/text()')
    print(text_list)

def test2():
    data = """
            <div>
                <ul>
                     <li class="item-0"><a href="link1.html">first item</a></li>
                     <li class="item-1"><a href="link2.html">second item</a></li>
                     <li class="item-inactive"><a href="link3.html">third item</a></li>
                     <li class="item-1" id="1" ><a href="link4.html">fourth item</a></li>
                     <li class="item-0" data="2"><a href="link5.html">fifth item</a>
                 </ul>
             </div>
            """

    html = etree.HTML(data)
    # 选取class为item-0的li标签
    li_list = html.xpath('//li[@class="item-0"]')
    print(li_list)
    print("-----------------------------------------")
    # 选取class为item-0的li标签 下面a标签的值
    text_list = html.xpath('//li[@class="item-0"]/a/text()')
    print(text_list)
    print("-----------------------------------------")
    # 选取id属性为1的li标签
    li1_list = html.xpath('//li[@id="1"]')
    print(li1_list)
    print("-----------------------------------------")
    # 选取data属性为2的li标签
    li2_list = html.xpath('//li[@data="2"]')
    print(li2_list)


def test3():
    data = """
            <div>
                <ul>
                     <li class="item-0"><a href="link1.html">first item</a></li>
                     <li class="item-1"><a href="link2.html">second item</a></li>
                     <li class="item-inactive"><a href="link3.html">third item</a></li>
                     <li class="item-1" id="1" ><a href="link4.html">fourth item</a></li>
                     <li class="item-0" data="2"><a href="link5.html">fifth item</a>
                 </ul>
             </div>
            """

    html = etree.HTML(data)
    # 选取ul下面的第一个li节点
    li_list = html.xpath('//ul/li[1]')
    print(li_list)
    print("-----------------------------------------")
    # 选取ul下面的最后一个li节点
    li1_list = html.xpath('//ul/li[last()]')
    print(li1_list)
    print("-----------------------------------------")
    # 选取ul下面的最后一个li节点
    li2_list = html.xpath('//ul/li[last()-1]')
    print(li2_list)
    print("-----------------------------------------")
    # 选取ul下面前3个标签
    li3_list = html.xpath('//ul/li[position()<= 3]')
    print(li3_list)
    print("-----------------------------------------")
    # 选取ul下面前3个标签的里面的a标签里面的href的值
    text_list = html.xpath('//ul/li[position()<= 3]/a/@href')
    print(text_list)

def test4():
    data = """
            <div>
                <ul>
                     <li class="item-0"><a href="link1.html">first item</a></li>
                     <li class="item-1"><a href="link2.html">second item</a></li>
                     <li class="item-inactive"><a href="link3.html">third item</a></li>
                     <li class="item-1" id="1" ><a href="link4.html">fourth item</a></li>
                     <li class="item-0" data="2"><a href="link5.html">fifth item</a>
                 </ul>
             </div>
            """

    html = etree.HTML(data)

    # 获取class包含以item-1开头的li标签
    li_list = html.xpath('//li[starts-with(@class,"item-1")]')
    print(li_list)
    print("-----------------------------------------")
    # 获取class包含item的li标签
    li1_list = html.xpath('//li[contains(@class,"item-1")]')
    print(li1_list)
    print("-----------------------------------------")
    # 获取class为item-0并且data为2的li标签
    li2_list = html.xpath('//li[contains(@class,"item-0") and contains(@data,"2")]')
    print(li2_list)
    print("-----------------------------------------")
    # 获取class为item-1或者data为2的li标签
    li3_list = html.xpath('//li[contains(@class,"item-1") or contains(@data,"2")]')
    print(li3_list)








if __name__ == '__main__':
    test4()
