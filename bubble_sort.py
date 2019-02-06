#!/usr/bin/env python
# encoding: utf-8


"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: bubble_sort.py
@time: 2019/1/10 21:17
"""


def bubble_sort(lyst):
    a = len(lyst)-1
    for x in range(a):
        print(x, ':', lyst)
        for y in range(a - x):
            if lyst[y] > lyst[y + 1]:
                lyst[y], lyst[y + 1] = lyst[y + 1], lyst[y]
    print('done', lyst)


lyst = [6, 2, 7, 1, 10, 3, 9, 4, 8, 5]
bubble_sort(lyst)
