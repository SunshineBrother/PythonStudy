# day01-字符串
 
## Python 访问字符串中的值
Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
Python 访问子字符串，可以使用方括号 `[]` 来截取字符串，字符串的截取的语法格式如下

```
var1 = "Runoob"
print ("var1[0]: ", var1[0])
print ("var1[1:5]: ", var1[1:5])

('var1[0]: ', 'R')
('var1[1:5]: ', 'unoo')
```

## Python 字符串连接
```
var2 = 'Hello World!'
var3 = var2[:6] + "Runoob"
print(var3)
Hello Runoob
```

## Python字符串运算符
```
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
```

## Python 三引号
Python 中三引号可以将复杂的字符串进行赋值。
Python 三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。
```
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)
```

## Python 的字符串内建函数
- 1、capitalize():将字符串的第一个字符转换为大写
```
str = "hello WORLD"
print(str.capitalize())
Hello world
需要注意的是：
1、首字符会转换成大写，其余字符会转换成小写。
2、首字符如果是非字母，首字母不会转换成大写，会转换成小写
```
- 2、center(width, fillchar)：返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。
    - width -- 字符串的总宽度。
    - fillchar -- 填充字符。
```
str1 = "[runoob]"
print ("str1.center(40, '*') : ", str1.center(40, '*'))
("str1.center(40, '*') : ", '****************[runoob]****************')
```
- 3、count(str, beg= 0,end=len(string))：返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    - sub -- 搜索的子字符串
    - start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
    - end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
```
str3="www.runoob.com"
print (str3.count("run",0,10)) //1
print(str3.count("o")) // 3
```
