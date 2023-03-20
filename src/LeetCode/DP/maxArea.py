#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : maxArea
@Software       : PyCharm
@Modify Time    : 2023/3/20 08:08
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            tmp_area = min(height[left], height[right]) * (right - left)
            res = max(res, tmp_area)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return res


if __name__ == '__main__':
    sol = Solution()

    height = [1, 2, 1]
    print(sol.maxArea(height))