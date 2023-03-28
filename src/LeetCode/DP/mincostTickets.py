#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : mincostTickets
@Software       : PyCharm
@Modify Time    : 2023/3/28 08:08
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for i in range(days[-1] + 1)]
        dy = set(days)
        for i in range(days[-1] + 1):
            if i not in dy:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 7)] + costs[1], dp[max(0, i - 1)] + costs[0], dp[max(0, i - 30)] + costs[2])

        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]
    print(sol.mincostTickets(days, costs))
