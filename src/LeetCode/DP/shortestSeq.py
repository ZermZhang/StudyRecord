#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : shortestSeq
@Software       : PyCharm
@Modify Time    : 2021/5/25 19:56
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


class Solution:
    @staticmethod
    def shortestSeq(big: List[int], small: List[int]) -> List[int]:
        # 双指针初始化
        left = 0
        min_len = len(big)
        res = []

        # 判断输入数组是否有效
        if big is None or small is None:
            return []
        if len(big) < len(small):
            return []

        for i in range(1, len(big)):
            right = i

            while set(small).issubset(set(big[left: right+1])):
                if min_len <= right - left:
                    pass
                else:
                    min_len = right - left
                    res = [left, right]
                left += 1
        return res

    @staticmethod
    def v2(big: List[int], small: List[int]) -> List[int]:
        import collections
        counters = collections.Counter(small)
        sub_seq = collections.defaultdict(int)

        left = 0
        right = 0
        res = []

        if big is None or small is None:
            return []
        if len(big) < len(small):
            return []

        def contains(a, b):
            if len(a) < len(b):
                return False
            for ele in b:
                if a[ele] < b[ele]:
                    return False
            return True

        while right < len(big):
            sub_seq[big[right]] += 1
            while contains(sub_seq, counters):
                if not res or right - left < res[1] - res[0]:
                    res = [left, right]
                sub_seq[big[left]] -= 1
                left += 1
            right += 1
        return res


if __name__ == '__main__':
    big_ = [521704, 897261, 279103, 381783, 668374, 934085, 254258, 726184, 496153, 804155]
    small_ = [897261, 9385, 381783, 496153]
    print(Solution.v2(big_, small_))
