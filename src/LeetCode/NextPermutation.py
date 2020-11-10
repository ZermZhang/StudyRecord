#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : NextPermutation
@Software       : PyCharm
@Modify Time    : 2020/11/10 08:11     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 31. 下一个排列
"""
from typing import List
import bisect


def nextPermutation(nums: List[int]) -> None:

    index = len(nums) - 1
    while index > 0:
        if nums[index] > nums[index - 1]:
            break
        index -= 1

    if index > 0:
        nums[index:] = sorted(nums[index:])
        swap_index = bisect.bisect(nums, nums[index - 1], lo=index)
        nums[swap_index], nums[index - 1] = nums[index - 1], nums[swap_index]
    else:
        nums.reverse()


if __name__ == "__main__":
    nums_example = [1, 2, 3]
    nextPermutation(nums_example)
    print(nums_example)
