# day04-循环结构
 
## if-else
```
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```

## while 循环
```
while 判断条件(condition)：
    执行语句(statements)……
```

**while 循环使用 else 语句**

如果 while 后面的条件语句为 false 时，则执行 else 的语句块。
语法格式如下：
```
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```

## for 语句

Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。
for循环的一般格式如下：
```
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```

![](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day04-循环结构/for.jpg)

```
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
```

**range()函数**
如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
```
for i in range(5):
    print(i)
0
1
2
3
4
```
你也可以使用range指定区间的值：
```
for i in range(5,9) :
    print(i)
```

也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
```
for i in range(0, 10, 3) :
    print(i)

0
3
6
9
```
您可以结合range()和len()函数以遍历一个序列的索引,如下所示:
```
sites = ["Baidu", "Google","Runoob","Taobao"]
for i in range(len(sites)):
    print(i,sites[i])

(0, 'Baidu')
(1, 'Google')
(2, 'Runoob')
(3, 'Taobao')
```
## 迭代器与生成器

```
list = [1,2,3,4]  
it = iter(list) //创建迭代器对象
print(next(it)) //输入迭代器下一个元素
print(next(it))

1
2
```

迭代器对象可以使用常规for语句进行遍历：
```
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")
```

也可以使用 next() 函数：
```
import sys         # 引入 sys 模块
 
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
 
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()
```









