#!/usr/bin/env python
# encoding: utf-8


"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: Longest Substring Without Repeating Characters.py
@time: 2019/1/10 20:08
"""
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_one = 0
        nums = 0
        test = ''
        for i in s:
            if i not in test:
                test += i
                nums += 1
            else:
                if nums >= max_one:
                    max_one = nums
                index = test.index(i)
                test = test[(index + 1):] + i
                nums = len(test)
        if nums > max_one:
            max_one = nums
        return max_one


s = Solution()
solution1 = s.lengthOfLongestSubstring("abcabcbb")
solution2 = s.lengthOfLongestSubstring("dvdf")
solution3 = s.lengthOfLongestSubstring("pwwkew")
solution4 = s.lengthOfLongestSubstring("")
solution5 = s.lengthOfLongestSubstring("  ")
print(solution1, solution2, solution3, solution4, solution5)
