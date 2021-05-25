#!/usr/bin/env python
# coding: utf-8


def write():
   f = open("/Users/yunna/Desktop/2.txt","w")
   f.write("你好，世界")
   f.close()

def read():
   f = open("/Users/yunna/Desktop/1.txt","r")
   str = f.read()
   print(str)
   f.close()
   

def readline():
   f = open("/Users/yunna/Desktop/1.txt","r")
   str = f.readline()
   print(str)
   f.close()


def readlines():
   f = open("/Users/yunna/Desktop/3.txt","r")
   str = f.readlines()
   print(str)
   f.close()




if __name__ == '__main__':
   # read()
   # print("----------------------------")
   # readline()
   # write()
   # print("----------------------------")
   readlines()
 
 







 












