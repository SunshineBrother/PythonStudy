# day02-列表
Python 有 6 个序列的内置类型，但最常见的是列表和元组。

## 列表
列表可以正向访问，也可以反向访问

![](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day02-列表/list1.png)

![](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day02-列表/list2.png)

```
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[1] ) //green
print( list[-1] ) //black
```
### 更新列表
```
list = ['Google', 'Runoob', 1997, 2000]
 
print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])
```
### 删除列表元素
```
list = ['Google', 'Runoob', 1997, 2000]
 
print ("原始列表 : ", list)
del list[2]
print ("删除第三个元素 : ", list)
```

### Python列表脚本操作符
- `+` 号用于组合列表
- `*` 号用于重复列表。
- `in` 元素是否存在于列表中,`3 in [1, 2, 3]`

### 常见函数
- 1、`len(list)`:列表元素个数
- 2、`list.append(obj)`:在列表末尾添加新的对象
- 3、`list.count(obj)`:统计某个元素在列表中出现的次数
- 4、`list.extend(seq)`:在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表
- 5、`list.index(obj)`:从列表中找出某个值第一个匹配项的索引位置
- 6、`list.insert(index, obj)`:将对象插入列表
- 7、`list.pop([index=-1])`:移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
- 8、`list.remove(obj)`:移除列表中某个值的第一个匹配项
- 9、`list.reverse()`:反向列表中元素
- 10、`list.sort( key=None, reverse=False)`:对原列表进行排序
- 11、`list.clear()`:清空列表
- 12、`list.copy()`:复制列表
 

## 元组
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号 `( )`，列表使用方括号 `[ ]`。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

```
tup1 = ('Google', 'Runoob', 1997, 2000)
```




















