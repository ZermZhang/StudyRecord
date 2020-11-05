#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : WordSolitaire
@Software       : PyCharm
@Modify Time    : 2020/11/5 08:29     
@Author         : zermzhang
@version        : 1.0
@Desciption     : 
"""

from typing import List
from collections import defaultdict
from collections import deque


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    size, general_dic = len(beginWord), defaultdict(list)

    for word in wordList:
        for _ in range(size):
            general_dic[word[:_] + "*" + word[_+1:]].append(word)

    queue = deque()
    queue.append((beginWord, 1))
    mark_dic = defaultdict(bool)
    mark_dic[beginWord] = True
    while queue:
        cur_word, level = queue.popleft()
        for i in range(size):
            for neighbour in general_dic[cur_word[:i] + "*" + cur_word[i+1:]]:
                if neighbour == endWord:
                    return level + 1
                if not mark_dic[neighbour]:
                    mark_dic[neighbour] = True
                    queue.append((neighbour, level + 1))
    return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(ladderLength(beginWord, endWord, wordList))
