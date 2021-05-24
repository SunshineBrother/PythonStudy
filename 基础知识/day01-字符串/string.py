#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# Python 访问字符串中的值

![](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day01-字符串/string1.png)

var1 = "Runoob"
print ("var1[0]: ", var1[0])
print ("var1[1:5]: ", var1[1:5])

# Python 字符串连接
var2 = 'Hello World!'
var3 = var2[:6] + "Runoob"
print(var3)
 

# Python字符串运算符
a = "hello "
b = "world"
print("a + b 字符串连接：",a+b)
print("重复输入字符串:",a*2)
print("通过索引获取字符串中字符:",a[2])
print("截取字符串中的一部分:",a[1:4])

# 成员运算符 - 如果字符串中包含给定的字符返回 True
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")

# 成员运算符 - 如果字符串中不包含给定的字符返回 True
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")


print (r'\n')
print (R'\n')

print ("我叫 %s 今年 %d 岁!" % ('小明', 10))


# Python 三引号
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)
 
# Python 的字符串内建函数
str = "hello WORLD"
print(str.capitalize())

str1 = "[runoob]"
print ("str1.center(40, '*') : ", str1.center(40, '*'))
 
str3="www.runoob.com"
print (str3.count("run",0,10))
print(str3.count("o"))





