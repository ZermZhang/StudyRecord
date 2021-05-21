#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : numIdenticalPairs
@Software       : PyCharm
@Modify Time    : 2021/5/21 14:13
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count


if __name__ == '__main__':
    nums_ = [1, 2, 3, 1, 1, 3]
    print(numIdenticalPairs(nums_))
