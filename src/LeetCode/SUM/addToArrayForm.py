from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a = num[::-1]
        b = [ele[1] for ele in enumerate(str(k))][::-1]

        a_len = len(a)
        b_len = len(b)

        if b_len > a_len:
            a, b = b, a
            a_len, b_len = b_len, a_len
        
        res = ''
        quotient = 0
        remainder = 0

        for i in range(a_len):
            if i < b_len:
                sum_ = int(a[i]) + int(b[i]) + quotient
            else:
                sum_ = int(a[i]) + quotient
            
            quotient = sum_ // 10
            remainder = sum_ % 10

            res = res + str(remainder)
        
        if quotient != 0:
            res = res + '1'
        return list(map(int, res[::-1]))


if __name__ == '__main__':
    sol = Solution()
    num = [2, 7, 4]
    k = 1813
    print(sol.addToArrayForm(num, k))