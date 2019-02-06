#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: Median of Two Sorted Arrays.py
@time: 2019/2/3 19:46
"""
"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，
并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        le = len(nums1 + nums2)
        if le % 2 == 1:
            return float(sorted(nums1 + nums2)[(le // 2)])
        else:
            return float((sorted(nums1 + nums2)[le // 2] + sorted(nums1 + nums2)[(le // 2) - 1]) / 2)


n1 = [1]
n2 = [3, 4]
s = Solution()
res = s.findMedianSortedArrays(n1, n2)
print(res)
