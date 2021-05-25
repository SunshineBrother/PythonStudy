# day06-文件I/O
 

## 读和写文件
open() 将会返回一个 file 对象，基本语法格式如下:
```
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
- file: 必需，文件路径（相对或者绝对路径）。
- mode: 可选，文件打开模式,决定了打开文件的模式：只读，写入，追加等。这个参数是非强制的，默认文件访问模式为只读(r)。
- buffering: 设置缓冲
- encoding: 一般使用utf8
- errors: 报错级别
- newline: 区分换行符
- closefd: 传入的file参数类型
- opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。



```
def write():
   f = open("/Users/yunna/Desktop/2.txt","w")
   f.write("你好，世界")
   f.close()

def read():
   f = open("/Users/yunna/Desktop/1.txt","r")
   str = f.read()
   print(str)
   f.close()
```

### f.readline()
`f.readline()` 会从文件中读取单独的一行。换行符为 `\n`。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
```
def readline():
   f = open("/Users/yunna/Desktop/1.txt","r")
   str = f.readline()
   print(str)
   f.close()
```

### f.readlines()
f.readlines() 将返回该文件中包含的所有行，返回的是数组
```
def readlines():
   f = open("/Users/yunna/Desktop/3.txt","r")
   str = f.readlines()
   print(str)
   f.close()

['123\n', '456']
```

另一种方式是迭代一个文件对象然后读取每行:
```
f = open("/Users/yunna/Desktop/3.txt", "r")

for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()
```


























 
