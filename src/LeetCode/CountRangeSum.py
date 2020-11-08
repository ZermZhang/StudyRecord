#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : CountRangeSum
@Software       : PyCharm
@Modify Time    : 2020/11/7 19:37     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""
from typing import List
import itertools
import bisect

def countRangeSum(nums: List[int], lower: int, upper: int) -> int:
    valid_range = []

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if (sum(nums[i:j+1]) >= lower) and (sum(nums[i:j+1]) <= upper):
                valid_range.append([i, j])

    return len(valid_range)


def countRangeSum_v2(nums: List[int], lower: int, upper: int) -> int:
    ans, q = 0, []
    for s in reversed((0, *itertools.accumulate(nums))):
        ans += bisect.bisect(q, s + upper) - bisect.bisect_left(q, s + lower)
        q[(k := bisect.bisect(q, s)): k] = [s]
    return ans


if __name__ == "__main__":
    nums_example = [-2, 5, -1]
    lower_example = -2
    upper_example = 2
    print(countRangeSum(nums_example, lower_example, upper_example))
