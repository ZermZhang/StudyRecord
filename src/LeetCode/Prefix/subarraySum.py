#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : subarraySum
@Software       : PyCharm
@Modify Time    : 2021/5/27 08:15
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        import collections
        sub_sum_ = collections.defaultdict(int)
        sub_sum_[0] = 1
        sum_tmp = 0

        subarray_cnt = 0

        for index in range(len(nums)):
            sum_tmp += nums[index]
            subarray_cnt += sub_sum_.get(sum_tmp - k, 0)
            sub_sum_[sum_tmp] = sub_sum_[sum_tmp] + 1

        return subarray_cnt


if __name__ == '__main__':
    nums = [1, 2, 3]
    k = 3
    solution = Solution()
    print(solution.subarraySum(nums, k))