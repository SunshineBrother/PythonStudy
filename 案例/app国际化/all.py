#!/usr/bin/env python
# coding: utf-8

import os
import json

def readlines_ios(file):
    dic = {}
    lines = []
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for item in lines:
        c = item.strip()
        if not c or c.startswith('//'):
            continue
        data = c.split('=')
        key = data[0].strip()
        value = data[1].strip()
        dic[key] = value
    return dic        

def readlines_android(file):
    dic = {}
    lines = []
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for item in lines:
        c = item.strip()
        if not c or not c.startswith('<string'):
            continue
        idx1 = c.find('name="')
        idx2 = c.find('">')
        idx3 = c.find('</string>')
        if idx1 < 0 or idx2 < 0 or idx3 < 0:
            continue
        name = c[idx1 + 6 : idx2]
        value = c[idx2 + 2 : idx3]
        dic[name] = value
    return dic        

def find_diff(file_cn, file_en, output_file, ostype):
    dic_cn, dic_en = {}, {}
    if ostype == 'android':
        dic_cn = readlines_android(file_cn)
        dic_en = readlines_android(file_en)
    elif ostype == 'ios':
        dic_cn = readlines_ios(file_cn)
        dic_en = readlines_ios(file_en)
    else:
        print('ostype error')
        return
    keys_cn = list(dic_cn.keys())
    keys_en = list(dic_en.keys())
    
    diff = [k for k in keys_cn if k not in keys_en]
    # print(len(diff))
    
    lines = [k + ' = ' + dic_cn[k] + '\n' for k in diff]
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
 
if __name__ == '__main__':

    # ostype = 'android'
    ostype = 'ios'
    file_cn = '/Users/yunna/Desktop/a/1.txt'
    file_en = '/Users/yunna/Desktop/a/2.txt'
    output_file = '/Users/yunna/Desktop/a/3.txt'

    find_diff(file_cn, file_en, output_file, ostype)
