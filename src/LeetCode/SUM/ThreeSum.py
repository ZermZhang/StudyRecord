#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : threeSum
@Software       : PyCharm
@Modify Time    : 2020/11/6 14:58     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 超出时间限制
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            valid_ = []

            for i in range(len(nums)):
                remain = target - nums[i]
                if remain in nums[i + 1:]:
                    valid_.append([nums[i], remain])

            return valid_

        target = 0
        returns = []

        for i in range(len(nums)):
            remain = target - nums[i]
            valid_remains = twoSum(nums[i+1:], remain)
            if len(valid_remains) != 0:
                valid_remains = [sorted(ele + [nums[i]]) for ele in valid_remains]
                for ele in valid_remains:
                    if ele in returns:
                        continue
                    else:
                        returns.append(ele)

        return returns

    def threeSum_v2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if (i > 0 and a == nums[i - 1]):
                # for duplicate of the first position...
                continue
            l, r = i + 1, len(nums) - 1
            while (l < r):
                three = a + nums[l] + nums[r]
                if (three > 0):
                    r -= 1
                elif (three < 0):
                    l += 1
                else:
                    p = []
                    p.append(a)
                    p.append(nums[l])
                    p.append(nums[r])
                    res.append(p)
                    while nums[l] == p[1] and l < r:
                        # second point duplicates...
                        l += 1
                    while nums[r] == p[2] and l < r:
                        # third point duplicactes...
                        r -= 1
        return res


if __name__ == "__main__":
    sol = Solution()
    nums_example = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums_example))
