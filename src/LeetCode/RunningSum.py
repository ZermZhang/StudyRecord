#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : RunningSum
@Software       : PyCharm
@Modify Time    : 2021/4/12 08:53
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


def runningSum(nums: List[int]) -> List[int]:
    return [sum(nums[:i + 1]) for i in range(len(nums))]


if __name__ == "__main__":
    nums_example = [3, 1, 2, 10, 1]
    print(runningSum(nums_example))
