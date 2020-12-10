#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : MaxSubArray
@Software       : PyCharm
@Modify Time    : 2020/12/10 08:08     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""
from typing import List


def max_sub_array(nums: List[int]) -> int:
    tmp = nums[0]
    max_ = tmp
    n = len(nums)
    for i in range(1, n):
        # 当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
        if tmp + nums[i] > nums[i]:
            max_ = max(max_, tmp + nums[i])
            tmp = tmp + nums[i]
        else:
            # 当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
            # 并记录此时的最大值
            max_ = max(max_, tmp, tmp + nums[i], nums[i])
            tmp = nums[i]
    return max_


if __name__ == "__main__":
    nums_example = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sub_array(nums_example))
