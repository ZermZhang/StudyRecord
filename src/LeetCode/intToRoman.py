#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : intToRoman
@Software       : PyCharm
@Modify Time    : 2020/11/1 21:25     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""


class Solution:
    @staticmethod
    def intToRoman(self, num: int) -> str:
        num_dict = {1: 'I',
                    4: 'IV',
                    5: 'V',
                    9: 'IX',
                    10: 'X',
                    40: 'XL',
                    50: 'L',
                    90: 'XC',
                    100: 'C',
                    400: 'CD',
                    500: 'D',
                    900: 'CM',
                    1000: 'M'}
        res = ""
        for key in sorted(num_dict.keys())[::-1]:
            if (num == 0):
                break
            tmp = num // key
            if (tmp == 0):
                continue
            res += num_dict[key] * (tmp)
            num -= key * (tmp)
        return res
