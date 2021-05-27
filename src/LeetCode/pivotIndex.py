#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : pivotIndex
@Software       : PyCharm
@Modify Time    : 2021/5/27 08:59
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 7772ms, 5.04%
        # 15.5MB, 97.17%
        pivot_index = -1
        for index in range(len(nums)):
            if sum(nums[0:index]) == sum(nums[index+1:]):
                pivot_index = index
                break
        return pivot_index

    def v2(self, nums: List[int]) -> int:
        # 64ms, 51.08%
        # 15.8MB, 381.0%
        all_sum = sum(nums)
        prefix_sum = 0

        pivot_index = -1

        for index in range(len(nums)):
            if all_sum - prefix_sum - nums[index] == prefix_sum:
                pivot_index = index
                break
            prefix_sum += nums[index]

        return pivot_index


if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    solution = Solution()
    print(solution.v2(nums))
