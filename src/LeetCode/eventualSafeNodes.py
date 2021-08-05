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

    def eventualSafeNodes_v2(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = set()
        ans = []

        def dfs(node: int) -> bool:
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            graph[node] = []
            visited.remove(node)
            return True

        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans


if __name__ == "__main__":
    solution = Solution()
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]

    safe_nodes = solution.eventualSafeNodes_v2(graph)
    print(f"the all safe nodes: {safe_nodes}")
