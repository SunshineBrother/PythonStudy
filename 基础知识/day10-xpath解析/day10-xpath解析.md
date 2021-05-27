# day10-xpath解析

把网站上的每页数据请求下来是爬虫的第一步，接下来我们就需要把每页上对我们有用数据进行提取。提取数据的方式有很多，比如说正则、xpath、bs4等，我们今天就来学一下xpath的语法。


## Xpath

**什么是xpath?**

XPath (XML Path Language) 是一门在 XML 文档中查找信息的语言，可用来在 XML 文档中对元素和属性进行遍历。

**什么是xml**

- XML 是一种标记语言，很类似 HTML
- XML 的设计宗旨是传输数据，而非显示数据
- XML 标签没有被预定义。您需要自行定义标签。
- XML 被设计为具有自我描述性。
- XML 是 W3C 的推荐标准

 ## 基础用法

XPath 使用路径表达式来选取 XML 文档中的节点或者节点集。这些路径表达式和我们在常规的电脑文件系统中看到的表达式非常相似。

| 表达式       | 含义                |
|------------|----------------------------|
|/|从根节点开始|
|//|从任意节点|
|.|从当前节点|
|..|从当前节点的父节点|
|@|选取属性|
|text()|选取文本|

```
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
```

打印

```
[<Element li at 0x7fac48169ec8>, <Element li at 0x7fac48169e88>, <Element li at 0x7fac48169f88>, <Element li at 0x7fac48169fc8>, <Element li at 0x7fac48177048>]
-----------------------------------------
[<Element a at 0x7fac481770c8>, <Element a at 0x7fac48177108>, <Element a at 0x7fac48177148>, <Element a at 0x7fac48177188>, <Element a at 0x7fac481771c8>]
-----------------------------------------
['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
-----------------------------------------
['first item', 'second item', 'third item', 'fourth item', 'fifth item']
```

我们发现最后打印的值都是一个列表对象，如果想取值就可以遍历列表了。


 ## 通配符

选取未知节点 XPath 通配符可用来选取未知的 XML 元素。



| 通配符       | 含义                |
|------------|----------------------------|
|*|选取任何元素节点|
|@*|选取任何属性的节点|


```
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




#打印
[<Element li at 0x7ff6dd1770c8>, <Element li at 0x7ff6dd177048>]
-----------------------------------------
['first item', 'fifth item']
-----------------------------------------
[<Element li at 0x7ff6dd177108>]
-----------------------------------------
[<Element li at 0x7ff6dd177048>]
```


## 路径表达式

| 通配符       | 含义                |
|------------|----------------------------|
|[?]|选取第几个节点|
|last()|选取最后一个节点|
|last()-1|选取倒数第二个节点|
|position()-1|选取前两个|


```
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



[<Element li at 0x7fc626169f88>]
-----------------------------------------
[<Element li at 0x7fc626169f08>]
-----------------------------------------
[<Element li at 0x7fc626169ec8>]
-----------------------------------------
[<Element li at 0x7fc626169f88>, <Element li at 0x7fc626169fc8>, <Element li at 0x7fc626178048>]
-----------------------------------------
['link1.html', 'link2.html', 'link3.html']
```







































