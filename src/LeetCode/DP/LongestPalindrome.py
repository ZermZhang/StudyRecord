#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : LongestPalindrome
@Software       : PyCharm
@Modify Time    : 2020/12/9 09:21     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""


def longest_palindrome_v1(s: str) -> str:
    if not s: return ""
    length = len(s)
    if length == 1 or s == s[::-1]: return s
    max_len, start = 1, 0
    for i in range(1, length):
        even = s[i - max_len:i + 1]
        odd = s[i - max_len - 1:i + 1]
        if i - max_len - 1 >= 0 and odd == odd[::-1]:
            start = i - max_len - 1
            max_len += 2
            continue
        if i - max_len >= 0 and even == even[::-1]:
            start = i - max_len
            max_len += 1
            continue
    return s[start:start + max_len]


if __name__ == "__main__":
    string_example = 'babad'
    print(longest_palindrome_v1(string_example))
