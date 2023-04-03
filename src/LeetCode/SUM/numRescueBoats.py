#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : numRescueBoats
@Software       : PyCharm
@Modify Time    : 2023/4/3 08:19
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_poeple = sorted(people)
        nums = 0
        left, right = 0, len(sorted_poeple) - 1

        while left < right:
            remain = limit - sorted_poeple[right]
            if remain < sorted_poeple[left]:
                nums += 1
                right -= 1
            else:
                nums += 1
                right -= 1
                left += 1
        if left == right:
            return nums + 1
        else:
            return nums


if __name__ == '__main__':
    sol = Solution()
    people = [5, 2, 1, 4]
    limit = 6
    print(sol.numRescueBoats(people, limit))
