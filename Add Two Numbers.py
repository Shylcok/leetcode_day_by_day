#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: Add Two Numbers.py
@time: 2019/2/3 15:46
"""
"""
给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        r = l3
        carry = 0
        res = []
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            # 相加的结果
            s = carry + x + y
            # 保存进位
            r = ListNode(s % 10)
            carry = s // 10
            res.append(r.val)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            r = r.next
        if carry == 1:
            res.append(1)
        return res


l1 = ListNode(5)
l2 = ListNode(5)

# 进位
s = Solution().addTwoNumbers(l1, l2)
print(s)
