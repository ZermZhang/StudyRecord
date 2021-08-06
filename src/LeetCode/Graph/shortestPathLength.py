#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : shortestPathLength.py
@Software       : PyCharm
@Modify Time    : 2021/8/6 15:55  
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""
from typing import List
import collections


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        edges = collections.defaultdict(list)
        for i in range(n):
            for j in range(len(graph[i])):
                edges[i].append(graph[i][j])

        # 状态压缩
        queue = []
        visited = set()
        for i in range(n):
            queue.append([1 << i, i, 0])
            visited.add((1 << i, i))

        # bfs
        while queue:
            len_ = len(queue)
            while len_:
                state, p, step = queue.pop(0)
                if state == (1 << n) - 1:
                    return step

                for next_node in graph[p]:
                    next_state = state | 1 << next_node
                    if (next_state, next_node) not in visited:
                        visited.add((next_state, next_node))
                        queue.append([next_state, next_node, step + 1])
                len_ -= 1


if __name__ == '__main__':
    graphs = [[1, 2, 3], [0], [0], [0]]
    solution = Solution()
    print(solution.shortestPathLength(graphs))
