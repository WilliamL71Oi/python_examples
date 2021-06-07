#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import islice


text = input("请输入md5密文： ")
if len(text) != 32:
    print('\n请输入32位长度的MD5密文。')
else:
    with open('60万条MD5密文.txt', 'r') as f:
        for line in f:
            if text == line.strip():
                r = '\n' + text + ' MD5解密为：'
                print(r, end='')
                print(''.join(islice(f, 1)))
                break
        else:
            print('\n您输入的MD5解密无匹配结果。')
            
