#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : maxProfit
@Software       : PyCharm
@Modify Time    : 2023/3/22 08:56
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
                continue
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
        return max_profit


if __name__ == '__main__':
    sol = Solution()
    prices = [7,6,4,3,1]
    print(sol.maxProfit(prices))