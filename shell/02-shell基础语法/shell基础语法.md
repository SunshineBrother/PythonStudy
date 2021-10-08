# shell基础语法

## 1、变量

定义变量时，变量名不加美元符号

```
name="xiaoming"
```

使用一个定义过的变量，只要在变量名前面加美元符号即可

```
echo $name
echo ${name}
```

变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界



## 2、Shell 字符串

字符串是shell编程中最常用最有用的数据类型，字符串可以用单引号，也可以用双引号，也可以不用引号。

```
str='this is a string'
str1="this is a string"
```

### 拼接字符串

```
echo "hello ${name}"
```

### 获取字符串长度

```
str='this is a string'
echo ${#str}
```

### 提取子字符串

```
string="runoob is a great site"
echo ${string:1:4} # 输出 unoo
```



## 3、Shell 数组

bash支持一维数组（不支持多维数组），并且没有限定数组的大小。

```
array_name=(value0 value1 value2 value3)
# 读取数组元素
echo $array_name[0]
# 取得数组元素的个数
length1=${#array_name[@]}
echo $length1
# 或者
length2=${#array_name[*]}
echo $length2
```



## 4、Shell 注释

以 **`#`** 开头的行就是注释，会被解释器忽略。

```
##### 用户配置区 开始 #####
#
#
# 这里可以添加脚本描述信息
# 
#
##### 用户配置区 结束  #####
```

### 多行注释

多行注释还可以使用以下格式：

```
:<<EOF
注释内容...
注释内容...
注释内容...
EOF
```



## 5、Shell 传递参数

我们可以在执行 Shell 脚本时，向脚本传递参数，脚本内获取参数的格式为：**$n**。**n** 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推……

```
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";
```































































