#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : ValidMountainArray
@Software       : PyCharm
@Modify Time    : 2020/11/3 09:49
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""

from typing import List


class Solution:
    @staticmethod
    def validMountainArray(nums: List[int]) -> bool:
        # 88ms, 100%; 14.3MB, 99.93%
        up, down = 0, 0

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return False
            if nums[i - 1] < nums[i]:
                if up == 0 and down == 0:
                    up = 1
                    continue
                if up == 1 and down == 0:
                    continue
                if up == 0 and down == 1:
                    return False
            if nums[i - 1] > nums[i]:
                if up == 1 and down == 0:
                    up = 0
                    down = 1
                if down == 1 and up == 0:
                    continue
                if up == 0 and down == 0:
                    return False
        return all([True, up == 0, down == 1])


if __name__ == "__main__":
    nums_example = []
    print(Solution.validMountainArray(nums_example))
