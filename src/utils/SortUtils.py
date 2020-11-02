#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : SortUtils
@Software       : PyCharm
@Modify Time    : 2020/11/2 18:43     
@Author         : zermzhang
@version        : 1.0
@Desciption     : the uilts for sort function
"""

from typing import List


class SortMethods:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums

    def bubble_sort(self) -> List[int]:
        for i in range(self.n):
            for j in range(1, self.n - i):
                if self.nums[j - 1] > self.nums[j]:
                    self.nums[j - 1], self.nums[j] = self.nums[j], self.nums[j - 1]
        return self.nums

    def selection_sort(self) -> List[int]:
        for i in range(self.n):
            for j in range(i, self.n):
                if self.nums[i] > self.nums[j]:
                    self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

    def insertion_sort(self) -> List[int]:
        for i in range(1, self.n):
            while i > 0 and self.nums[i - 1] > self.nums[i]:
                self.nums[i - 1], self.nums[i] = self.nums[i], self.nums[i - 1]
                i -= 1
        return self.nums

    def shell_sort(self):
        gap = self.n // 2
        while gap:
            for i in range(gap, self.n):
                while i - gap >= 0 and self.nums[i - gap] > self.nums[i]:
                    self.nums[i - gap], self.nums[i] = self.nums[i], self.nums[i - gap]
                    i -= gap
            gap //= 2
        return self.nums


if __name__ == "__main__":
    nums_example = [6, 5, 3, 1, 8, 7, 2, 4]
    print(SortMethods(nums_example).shell_sort())
