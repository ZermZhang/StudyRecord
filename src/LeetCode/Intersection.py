#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : intersection
@Software       : PyCharm
@Modify Time    : 2020/11/2 09:16     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""
from typing import List


class Solution:
    @staticmethod
    def intersection_v1(nums1: List[int], nums2: List[int]) -> List[int]:
        # 暴力穷举法
        # 84ms, 24.82%; 13.6MB, 11.02%
        res = []
        for num in set(nums1):
            if num in set(nums2):
                res.append(num)
        return res

    @staticmethod
    def intersection_v2(nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用dict进行位置存储
        # 64ms, 54.33%; 13.6MB, 9.88%
        res = []
        memories = {}

        for num in nums1:
            if num in memories:
                continue
            else:
                memories[num] = 1

        for num in nums2:
            if num in memories and memories[num] == 1:
                res.append(num)
                memories[num] += 1
            else:
                continue

        return res

    @staticmethod
    def intersection_v3(nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        return res


if __name__ == '__main__':
    nums1_example = [1, 2, 2, 1]
    nums2_example = [2, 2]
    print(Solution.intersection_v2(nums1_example, nums2_example))
