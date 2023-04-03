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
        """
        :param people:
        :param limit:
        :return:
        """
        # 先对人员的信息进行排序处理，从大到小或者从小到大
        sorted_poeple = sorted(people)
        nums = 0
        # 使用双指针对数组进行处理
        left, right = 0, len(sorted_poeple) - 1

        while left < right:
            # 计算当前两个指针分别指向的结果是否能够满足limit
            remain = limit - sorted_poeple[right]
            # 如果不能满足的话，说明右侧指针的结果已经是偏大了，无法和最小的值匹配上
            # 所以right对应的结果自己就要占据一个位置
            # right - 1，left不动
            if remain < sorted_poeple[left]:
                nums += 1
                right -= 1
            else:
                # 满足要求的话，可以让left和right都走一步
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
