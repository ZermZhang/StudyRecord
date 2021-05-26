#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : numMatchingSubseq
@Software       : PyCharm
@Modify Time    : 2021/5/26 15:27
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from typing import List


class Solution:
    # 写成寻找子集的逻辑了
    @staticmethod
    def numMatchingSubseq(s: str, words: List[str]) -> int:
        import collections
        counters = collections.Counter(s)
        match_num = len(words)

        for word in words:
            word_counter = collections.Counter(word)
            for ele in word_counter.keys():
                if word_counter[ele] > counters[ele] or ele not in counters:
                    match_num -= 1
                    break

        return match_num

    def numMatchingSubseq_v2(self, S: str, words: List[str]) -> int:
        count = 0
        for word in words:
            if self.isSubsequence(word, S):
                count += 1
            else:
                print(word)

        return count

    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        s = list(s)
        for _t in t:
            if not s:
                return True
            if _t == s[0]:
                s.pop(0)
        return len(s) == 0

    @staticmethod
    def numMatchingSubseq_v3(S: str, words: List[str]) -> int:
        import collections
        words_dict = collections.Counter(words)
        words_dict = dict([(ele, [[0, 0], 0, value]) for ele, value in words_dict.items()])

        for letter in S:
            for word in words:
                right = words_dict[word][0][1]
                if right >= len(word):
                    continue
                if letter == word[right]:
                    words_dict[word][1] = 1
                    words_dict[word][0][1] += 1

        match_num = 0
        for word, value in words_dict.items():
            if value[0][1] == len(word):
                match_num += (1 * value[2])

        return match_num

    @staticmethod
    def numMatchingSubseq_v4(S: str, words: List[str]) -> int:
        import collections
        waiting = collections.defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))

        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])


if __name__ == '__main__':
    s_ = "qlhxagxdqh"
    words_ = ["qlhxagxdq", "qlhxagxdq", "lhyiftwtut", "yfzwraahab"]

    solution = Solution()
    print(solution.numMatchingSubseq_v4(s_, words_))
