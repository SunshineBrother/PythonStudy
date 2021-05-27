# PythonStudy

Python学习项目

## 标准库
**操作系统接口**
```
import os

os.getcwd()      # 返回当前的工作目录
os.chdir('/server/accesslogs')   # 修改当前的工作目录
```

**文件通配符**
```
import glob
f = glob.glob("*.py")

['all.py', 'demo1.py']
```

**命令行参数**
通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。
```
import sys

print(sys.argv)
['demo.py', 'one', 'two', 'three']
```

**字符串正则匹配**
re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:

```
import re

re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']

re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
```

**数学**
```
import math

math.cos(math.pi / 4)
0.70710678118654757
```
 

## 基础知识
- [day01-字符串](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day01-字符串/day01-字符串.md)
- [day02-列表](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day02-列表/day02-列表.md)
- [day03-字典](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day03-字典/day03-字典.md)
- [day04-循环结构](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day04-循环结构/day04-循环结构.md)
- [day05-函数](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day05-函数/day05-函数.md)
- [day06-文件I/O](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day06-文件I:O/day06-文件I:O.md)
- [day07-异常](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day07-异常/day07-异常.md)
- [day08-对象](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day08-对象/day08-对象.md)
- [day09-网络](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day09-网络/day09-网络.md)
- [day10-xpath解析](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day10-xpath解析/day10-xpath解析.md)
 

 


## 案例
- [app国际化](https://github.com/SunshineBrother/PythonStudy/blob/main/案例/app国际化/all.py)
























