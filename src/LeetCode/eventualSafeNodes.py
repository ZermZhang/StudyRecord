#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : eventualSafeNodes.py
@Software       : PyCharm
@Modify Time    : 2021/8/5 17:10  
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""
from typing import List


class Solution:
    def get_end(self, sub_graph: List[List[int]],
                end_point: List[int]) -> List[int]:
        return [i for i in range(len(sub_graph)) if set(sub_graph[i]).issubset(end_point)]

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        sub_ends = []
        ends = self.get_end(graph, sub_ends)

        while len(ends) != len(sub_ends):

            sub_ends = ends
            ends = self.get_end(graph, sub_ends)

        return ends


if __name__ == "__main__":
    solution = Solution()
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]

    safe_nodes = solution.eventualSafeNodes(graph)
    print(f"the all safe nodes: {safe_nodes}")
