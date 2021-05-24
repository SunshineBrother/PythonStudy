# day03-字典
 

## 字典
可以取任何数据类型，但键必须是不可变的，如字符串，数字。
```
dict = { 'abc': 123, 98.6: 37 }
print(dict["abc"])
print(dict[98.6])
```
### 修改字典
```
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
dict['Age'] = 8               # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息
 
 
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
```

### 删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。
显示删除一个字典用del命令，如下实例：
```
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
del dict         # 删除字典
```

### 字典内置函数
- 1、`len(dict)`:计算字典元素个数，即键的总数
- 2、`str(dict)`:输出字典，以可打印的字符串表示。
```
dict = { 'abc': 123, 98.6: 37 }
print(str(dict))

{98.6: 37, 'abc': 123}
```
- 3、`clear()`:删除字典内所有元素
- 4、`get(key, default=None)`:返回指定键的值，如果键不在字典中返回 default 设置的默认值
- 5、`key in dict`:如果键在字典dict里返回true，否则返回false
- 6、`items()`:Python 字典 items() 方法以列表返回视图对象，是一个可遍历的key/value 对。
```
dict = { 'abc': 123, 98.6: 37 }
print(dict.items())
[(98.6, 37), ('abc', 123)]
```
- 7、`keys()`:所有的key
- 8、`values()`:values数组
- 9、`pop(key[,default])`:删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
 



 



















