class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        max_sub1 = self.getMaxSub(str1)
        max_sub2 = self.getMaxSub(str2)

        if max_sub1 == max_sub2:
            return max_sub1
        return ''

    def getMaxSub(self, s: str) -> str:
        sub_len = 1

        while sub_len < len(s):
            if s[:sub_len] != s[-sub_len:]:
                sub_len += 1
                continue
            else:
                break
        return s[:sub_len]


if __name__ == '__main__':
    str1 = "LEET"
    str2 = "CODE"
    sol = Solution()
    print(sol.gcdOfStrings(str1, str2))
    # print(sol.getMaxSub(str1))
