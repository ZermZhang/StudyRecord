#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : maxScoreSightseeingPair
@Software       : PyCharm
@Modify Time    : 2021/5/23 16:11
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


class Solution:
    @staticmethod
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                tmp_score = values[i] + values[j] + i - j
                if tmp_score >= max_score:
                    max_score = tmp_score
                else:
                    pass
        return max_score

    @staticmethod
    def v2(values: List[int]) -> int:
        max_score = 0
        length = len(values)

        if length == 0:
            return 0
        if length == 1:
            return values[0]

        dp = values[0] * 2
        for i in range(1, length):
            dp = max(dp - values[i - 1] + values[i] - 1, values[i - 1] + values[i] - 1)
            max_score = max(dp, max_score)
        return max_score


if __name__ == '__main__':
    values_ = [8, 1, 5, 2, 6]
    print(Solution.v2(values_))
