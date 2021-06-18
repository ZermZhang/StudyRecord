#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : smallestGoodBase
@Software       : PyCharm
@Modify Time    : 2021/6/18 11:30
@Author         : zermzhang
@version        : 1.0
@Desciption     : 最小好进制
"""


class Solution:
    @staticmethod
    def smallestGoodBase(n: str) -> str:
        num = int(n)

        for m in range(num.bit_length(), 2, -1):
            x = int(pow(num, 1/(m-1)))
            if num == (pow(x, m) - 1) // (x - 1):
                return str(x)
        return str(num - 1)


if __name__ == '__main__':
    inputs = '13'
    print(Solution.smallestGoodBase(inputs))
