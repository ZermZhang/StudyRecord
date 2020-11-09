#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : KC'losest
@Software       : PyCharm
@Modify Time    : 2020/11/9 08:24     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 973. 最接近原点的K个点
"""
from typing import List
from collections import defaultdict


def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
    # 696ms, 96.45%; 19.1 MB, 15.69%
    res = []
    distance = defaultdict(list)

    for i in range(len(points)):
        distance[points[i][0] * points[i][0] +
                 points[i][1] * points[i][1]].append(points[i])

    closest_k = sorted(distance)[:K]

    for k in closest_k:
        if len(res) < K:
            res.extend(distance[k])
        else:
            break

    return res


if __name__ == "__main__":
    points_example = [[1, 0], [0, 1]]
    K_example = 2
    print(kClosest(points_example, K_example))
