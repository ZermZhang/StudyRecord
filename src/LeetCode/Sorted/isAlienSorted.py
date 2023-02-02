from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda word: [order.index(c) for c in word])


if __name__ == '__main__':
    sol = Solution()
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(sol.isAlienSorted(words, order))
