#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : MaxProfit
@Software       : PyCharm
@Modify Time    : 2020/11/8 12:14     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""
from typing import List
import numpy as np


def maxProfit(prices: List[int]) -> int:
    # 60ms, 99.7%; 14.5MB, 78.28%
    if len(prices) == 0:
        return 0

    low_price = prices[0]
    best_profit = 0
    best_profits = 0

    for i in range(1, len(prices)):
        if prices[i] < low_price or prices[i] - low_price < best_profit:
            best_profits += best_profit
            low_price = prices[i]
            best_profit = 0
        elif prices[i] - low_price > best_profit:
            best_profit = prices[i] - low_price

    best_profits += best_profit

    return best_profits


if __name__ == "__main__":
    prices_example = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices_example))
