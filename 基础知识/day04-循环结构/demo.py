#!/usr/bin/env python
# coding: utf-8

import sys         # 引入 sys 模块
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")




# for i in range(5):
#     print(i)

# for i in range(5,9) :
#     print(i)

for i in range(0, 10, 3) :
    print(i)



for i in range(len(sites)):
    print(i,sites[i])


print("-----------------------")
list1 = [1,2,3,4]
it = iter(list1)
print(next(it))
print(next(it))

list2=[1,2,3,4]
it = iter(list2)    # 创建迭代器对象
for x in it:
    print (x, end=" ")



print("-----------------------")

 
list3=[1,2,3,4]
it = iter(list3)    # 创建迭代器对象

while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()












