#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : maxSatisfaction
@Software       : PyCharm
@Modify Time    : 2023/3/30 07:55
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction, reverse=True)

        sum_ = 0
        max_sat = 0

        for ele in satisfaction:
            if sum_ + ele > 0:
                max_sat = max_sat + sum_ + ele
                sum_ = sum_ + ele
        return max_sat


if __name__ == '__main__':
    sol = Solution()

    satisfaction = [-1, -8, 0, 5, -9]
    print(sol.maxSatisfaction(satisfaction))
