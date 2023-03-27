#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : longestCycle
@Software       : PyCharm
@Modify Time    : 2023/3/27 07:59
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


class Solution:
    def isCycle(self, idx: int, edges: List[int]) -> (List[int], bool):
        cycle = []
        # idx = edges[idx]
        flag = True
        if edges[idx] == -1:
            return cycle, False
        while idx not in cycle and edges[idx] != -1:
            cycle.append(idx)
            idx = edges[idx]
        if idx == -1 or idx != cycle[0]:
            flag = False
        return cycle, flag

    def longestCycle(self, edges: List[int]) -> int:
        max_cycle = -1
        for idx in range(len(edges)):
            cycle, flag = self.isCycle(idx, edges)
            if flag:
                max_cycle = max(max_cycle, len(cycle))

        return max_cycle


if __name__ == '__main__':
    sol = Solution()

    edges = [3, 3, 4, 2, 3]
    # edges = [2, -1, 3, 1]
    print(sol.longestCycle(edges))
    # print(sol.isCycle(1, edges))
