#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : TwoSum
@Software       : PyCharm
@Modify Time    : 2020/11/2 09:12     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""
from typing import List


class Solution:
    @staticmethod
    def twoSum_v1(nums: List[int], target: int) -> List[int]:
        # 执行用时：6000 ms, 在所有Python3提交中击败了16.41 % 的用户
        # 内存消耗：14.2 MB, 在所有Python3提交中击败了65.31 % 的用户
        # 暴力检索，两个for循环叠加
        indexs = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    indexs.extend([i, j])

        return indexs

    @staticmethod
    def twoSum_v2(nums: List[int], target: int) -> List[int]:
        # 44ms, 85.09%; 15.2MB, 6.31%
        # 通过dict存储遍历过的每个元素，然后去检索是否存在，用空间换时间
        mapping = {}
        indexs = []

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in mapping:
                indexs.extend([i, mapping[remain]])
            else:
                mapping[nums[i]] = i

        return indexs


if __name__ == "__main__":
    nums_example = [2, 7, 11, 15]
    target_example = 9
    print(Solution.twoSum_v2(nums_example, target_example))
