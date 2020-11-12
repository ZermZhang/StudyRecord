#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : SortArrayByParity
@Software       : PyCharm
@Modify Time    : 2020/11/12 08:27     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 922. 按奇偶排序数组II
"""
from typing import List


def sortArrayByParityII(A: List[int]) -> List[int]:
    # 228ms, 93.58%; 16.1MB, 5.35%
    res = []
    odds = []
    evens = []
    for ele in A:
        if ele % 2 == 0:
            evens.append(ele)
        else:
            odds.append(ele)

    for i in range(len(odds)):
        res.append(evens[i])
        res.append(odds[i])

    return res


if __name__ == "__main__":
    nums = [4, 2, 5, 7]
    print(sortArrayByParityII(nums))
