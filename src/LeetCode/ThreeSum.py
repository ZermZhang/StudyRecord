#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : threeSum
@Software       : PyCharm
@Modify Time    : 2020/11/6 14:58     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    # 超出时间限制
    def twoSum(nums: List[int], target: int) -> List[List[int]]:
        valid_ = []

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in nums[i + 1:]:
                valid_.append([nums[i], remain])

        return valid_

    target = 0
    returns = []

    for i in range(len(nums)):
        remain = target - nums[i]
        valid_remains = twoSum(nums[i+1:], remain)
        if len(valid_remains) != 0:
            valid_remains = [sorted(ele + [nums[i]]) for ele in valid_remains]
            for ele in valid_remains:
                if ele in returns:
                    continue
                else:
                    returns.append(ele)

    return returns


if __name__ == "__main__":
    nums_example = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums_example))
