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

        def skip_all_star(string, now_idx):
            step = 1
            while string[now_idx + step] == '*' or string[now_idx] == string[now_idx + step]:
                step += 1
                if now_idx + step < len(string):
                    continue
                else:
                    break
            return now_idx + step

        p_idx = 0
        s_idx = 0
        while p_idx < len(p) and s_idx < len(s):
            if p_idx + 1 < len(p) and p[p_idx + 1] == '*':
                now_s_ele = s[s_idx]
                if now_s_ele != p[p_idx] and p[p_idx] != '.':
                    p_idx = skip_all_star(p, p_idx)
                    continue
                else:
                    p_idx = skip_all_star(p, p_idx)
                    if p_idx == len(p):
                        return True
                    while now_s_ele == s[s_idx]:
                        s_idx += 1
                        if s_idx < len(s):
                            continue
                        else:
                            break
            elif p[p_idx] == s[s_idx] or p[p_idx] == '.':
                p_idx += 1
                s_idx += 1
                continue
            else:
                return False

        result_bool = True if s_idx == len(s) and p_idx == len(p) else False

        return result_bool
    
    
if __name__ == '__main__':
    s = "aaa"
    p = "ab*a*c*a"
    
    print(Solution.isMatch(s, p))
