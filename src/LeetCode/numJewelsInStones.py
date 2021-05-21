#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : numJewelsInStones
@Software       : PyCharm
@Modify Time    : 2021/5/21 13:43
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""


def numJewelsInStones(jewels: str, stones: str) -> int:
    count = 0
    for s in stones:
        if s in jewels:
            count += 1
    return count


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(J, S))
