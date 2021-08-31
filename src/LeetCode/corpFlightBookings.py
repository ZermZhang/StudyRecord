#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : corpFlightBookings.py
@Software       : PyCharm
@Modify Time    : 2021/8/31 16:58  
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for booking in bookings:
            first = booking[0]
            last = booking[1]
            seat = booking[2]
            for i in range(first - 1, last):
                res[i] += seat

        return res

    def corpFlightBookings_v2(self, bookings: List[List[int]], n: int) -> List[int]:
        l = len(bookings)
        ans = [0] * (n + 1)
        for i in range(l):
            ans[bookings[i][0] - 1] += bookings[i][2]
            ans[bookings[i][1]] -= bookings[i][2]
        for i in range(1, n + 1):
            ans[i] += ans[i - 1]
        return ans[:-1]
