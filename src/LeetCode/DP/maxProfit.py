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

        # 声明双指针，左侧标明最低价、右侧遍历所有的价格
        # 右侧的指针逐渐走动，左侧的指针根据条件进行变动
        # 如果出现了一个比left价格更低的情况，进行调整
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
                continue
            else:
                # 计算最大利润并记录
                max_profit = max(max_profit, prices[right] - prices[left])
        return max_profit


if __name__ == '__main__':
    sol = Solution()
    prices = [7,6,4,3,1]
    print(sol.maxProfit(prices))