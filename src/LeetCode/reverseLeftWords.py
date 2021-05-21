#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : reverseLeftWords
@Software       : PyCharm
@Modify Time    : 2021/5/21 10:03
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""


def reverseLeftWords(s: str, n: int) -> str:
    tmp_1 = ''
    tmp_2 = ''
    for i in range(len(s)):
        if i < n:
            tmp_1 += s[i]
        else:
            tmp_2 += s[i]
    return tmp_2 + tmp_1


def reverseLeftWords_v2(s: str, n: int) -> str:
    return s


if __name__ == "__main__":
    s = ""
    k = 2
    print(reverseLeftWords_v2(s, k))
