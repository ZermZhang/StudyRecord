#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : kidsWithCandies
@Software       : PyCharm
@Modify Time    : 2021/5/21 16:55
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)

    res = []
    for ele in candies:
        if max_candies - ele <= extraCandies:
            res.append(True)
        else:
            res.append(False)
    return res


if __name__ == '__main__':
    candies_ = [4,2,1,1,2]
    extraCandies_ = 1
    print(kidsWithCandies(candies_, extraCandies_))
