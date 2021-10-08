#!/bin/bash

a=10
b=20

# +
val1=`expr $a + $b`
echo "a + b : $val1"

# -
val=`expr $a - $b`
echo "a - b : $val"

# *
val3=`expr $a \* $b`
echo "a * b : $val3"

# /
val4=`expr $b / $a`
echo "b / a : $val4"

# %
val5=`expr $b % $a`
echo "b % a : $val5"

# 判等
if [ $a == $b ]
then
   echo "a 等于 b"
fi
if [ $a != $b ]
then
   echo "a 不等于 b"
fi


file="/Users/jiangjunhui/Desktop/test.sh"
if [ -r $file ]
then
   echo "文件可读"
else
   echo "文件不可读"
fi
if [ -w $file ]
then
   echo "文件可写"
else
   echo "文件不可写"
fi
if [ -x $file ]
then
   echo "文件可执行"
else
   echo "文件不可执行"
fi
if [ -f $file ]
then
   echo "文件为普通文件"
else
   echo "文件为特殊文件"
fi
if [ -d $file ]
then
   echo "文件是个目录"
else
   echo "文件不是个目录"
fi
if [ -s $file ]
then
   echo "文件不为空"
else
   echo "文件为空"
fi
if [ -e $file ]
then
   echo "文件存在"
else
   echo "文件不存在"
fi






















