#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : SortByBits
@Software       : PyCharm
@Modify Time    : 2020/11/6 07:45     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""
from typing import List
from collections import defaultdict


def sortByBits(arr: List[int]) -> List[int]:
    # 44ms, 96.05%; 13.6MB, 13.85%
    res = []
    cnt_mapping = defaultdict(list)
    for ele in arr:
        one_cnt = bin(ele).count('1')
        cnt_mapping[one_cnt].append(ele)

    for ele in sorted(cnt_mapping):
        res.extend(sorted(cnt_mapping[ele]))

    return res


if __name__ == "__main__":
    arr_example = [2, 3, 5, 7, 11, 13, 17, 19]
    print(sortByBits(arr_example))
