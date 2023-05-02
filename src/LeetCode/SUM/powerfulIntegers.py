#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : powerfulIntegers
@Software       : PyCharm
@Modify Time    : 2023/5/2 09:16
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from math import log
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        x_pows = []
        y_pows = []

        for i in range(bound):
            x_pow = pow(x, i)
            if x_pow >= bound:
                break
            else:
                x_pows.append(x_pow)

        for i in range(bound):
            y_pow = pow(y, i)
            if y_pow >= bound:
                break
            else:
                y_pows.append(y_pow)

        res = []
        for x_ele in x_pows:
            for y_ele in y_pows:
                sum_ = x_ele + y_ele
                if sum_ <= bound:
                    res.append(sum_)
                else:
                    pass
        return list(set(res))

    def powerfulIntegers_v2(self, x: int, y: int, bound: int) -> List[int]:
        imax, jmax, ans = 1 if x == 1 else round(log(max(1, bound - 1), x)) + 1, 1 if y == 1 else round(log(max(1, bound - 1), y)) + 1, set()
        for i in range(imax):
            for j in range(jmax):
                z = x ** i + y ** j
                if z <= bound:
                    ans.add(z)
        return list(ans)


if __name__ == '__main__':
    sol = Solution()
    x = 3
    y = 5
    bound = 15
    print(sol.powerfulIntegers(x, y, bound))
