#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : maximumWealth
@Software       : PyCharm
@Modify Time    : 2021/5/21 13:57
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
    user_wealth = []
    for i in range(len(accounts)):
        user_wealth.append(sum(accounts[i]))
    return max(user_wealth)


def maximumWealth_v2(accounts: List[List[int]]) -> int:
    return max([sum(ele) for ele in accounts])


def maximumWealth_v3(accounts: List[List[int]]) -> int:
    max_wealth_user = 0
    for ele in accounts:
        tmp = sum(ele)
        if tmp > max_wealth_user:
            max_wealth_user = tmp
    return max_wealth_user


if __name__ == '__main__':
    accounts_ = [[1,5],[7,3],[3,5]]
    print(maximumWealth_v3(accounts_))
