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
- 1、`capitalize()`:将字符串的第一个字符转换为大写
```
str = "hello WORLD"
print(str.capitalize())
Hello world
需要注意的是：
1、首字符会转换成大写，其余字符会转换成小写。
2、首字符如果是非字母，首字母不会转换成大写，会转换成小写
```
- 2、`center(width, fillchar)`：返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。
    - width -- 字符串的总宽度。
    - fillchar -- 填充字符。
```
str1 = "[runoob]"
print ("str1.center(40, '*') : ", str1.center(40, '*'))
("str1.center(40, '*') : ", '****************[runoob]****************')
```
- 3、`count(str, beg= 0,end=len(string))`：返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    - sub -- 搜索的子字符串
    - start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
    - end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
```
str3="www.runoob.com"
print (str3.count("run",0,10)) //1
print(str3.count("o")) // 3
```

- 4、`decode()`：decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
    - encoding -- 要使用的编码，如"UTF-8"。
    - errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。

- 5、`encode()`：`encode()` 方法以指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
    - `str.encode(encoding='UTF-8',errors='strict')`

- 6、`endswith(suffix, beg=0, end=len(string))`:检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

- 7、`find(str, beg=0, end=len(string))`:检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

- 8、`index(str, beg=0, end=len(string))`:跟find()方法一样，只不过如果str不在字符串中会报一个异常。
```
str1 = "Runoob example....wow!!!"
str2 = "exam";

print (str1.index(str2))
print (str1.index(str2, 5))
print (str1.index(str2, 10))

7
7
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    print (str1.index(str2, 10))
ValueError: substring not found
```
- 9、`isalnum()`:检测字符串是否由字母和数字组成。
- 10、`isalpha()`: isalpha() 方法检测字符串是否只由字母或文字组成。
- 11、`isdigit()`:检测字符串是否只由数字组成
- 12、`isnumeric()`:检测字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字。
- 13、`join()`:用于将序列中的元素以指定的字符连接生成一个新的字符串。
```
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq )) //r-u-n-o-o-b 
print (s2.join( seq )) //runoob
```
- 14、`len( s )`:方法返回对象（字符、列表、元组等）长度或项目个数。
- 15、`ljust()`:返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
```
str = "Runoob example....wow!!!"
print (str.ljust(50, '*'))

Runoob example....wow!!!**************************
```
- 16、`replace(old, new [, max])`:把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。
```
str = "www.w3cschool.cc"
print ("菜鸟教程旧地址：", str)
print ("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))
 
str = "this is string example....wow!!!"
print (str.replace("is", "was", 3))

菜鸟教程旧地址： www.w3cschool.cc
菜鸟教程新地址： www.runoob.com
thwas was string example....wow!!!
```
- 17、`split(str="", num=string.count(str))`:以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串







