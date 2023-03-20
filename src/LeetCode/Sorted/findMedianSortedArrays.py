#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : findMedianSortedArrays
@Software       : PyCharm
@Modify Time    : 2023/3/17 08:35
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merg = nums1.copy()
        merg.extend(nums2)
        merg.sort()

        if len(merg) % 2 != 0:
            return float((merg[len(merg) // 2]))
        else:
            a = merg[len(merg) // 2 - 1]
            b = merg[len(merg) // 2]
            return float((a + b) / 2)


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))