#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : SortedArray.py
@Software       : Spyder
@Modify Time    : 7/19 22:20     
@Author         : zermelzhang
@version        : 1.0
@Desciption     : None
"""


class Solution:
    @staticmethod
    def isMatch(s: str, p: str) -> bool:
        idx_p = 0
        dot_flag = 0
        star_flag = 0
        keep_ele = ''
        for idx_s in range(len(s)):
            if s[idx_s] == p[idx_p]:
                idx_p += 1
                dot_flag = 0
                star_flag = 0
                keep_ele = s[idx_s]
                continue
            if p[idx_p] == '.':
                idx_p += 1
                dot_flag = 1
                star_flag = 0
                keep_ele = s[idx_s]
                continue
            if p[idx_p] == '*' or star_flag == 1:
                if dot_flag == 1:
                    if idx_p == len(p) - 1:
                        return True
                    else:
                        return False
                elif dot_flag == 0 and s[idx_s] == keep_ele:
                    idx_p += 1
                    dot_flag = 0
                    star_flag = 1
                    keep_ele = s[idx_s]
                    continue
                else:
                    return False

        return True
    
    
if __name__ == '__main__':
    s = "aab"
    p = "c*a*b"
    
    print(Solution.isMatch(s, p))
