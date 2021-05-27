#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : missingNumber
@Software       : PyCharm
@Modify Time    : 2021/5/27 08:10
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i


if __name__ == '__main__':
    nums_ = [0]
    solution = Solution()
    print(solution.missingNumber(nums_))
