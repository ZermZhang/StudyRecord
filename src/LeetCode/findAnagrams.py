from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        sorted_p = sorted(p)

        output_list = []

        for i in range(len(s) - length + 1):
            if sorted(s[i:i+length]) == sorted_p:
                output_list.append(i)

        return output_list

    def findAnagrams_v2(self, s: str, p: str) -> List[int]:
        LS, LP, S, P, A = len(s), len(p), 0, 0, []

        if LP > LS:
            return []

        for i in range(LP):
            S, P = S + hash(s[i]), P + hash(p[i])

        if S == P:
            A.append(0)

        for i in range(LP, LS):
            S += hash(s[i]) - hash(s[i-LP])
            if S == P:
                A.append(i-LP+1)
        return A


if __name__ == '__main__':
    sol = Solution()
    s = "cbaebabacd"
    p = "abc"
    print(sol.findAnagrams_v2(s, p))
