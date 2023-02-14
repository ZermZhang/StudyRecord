class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        
        a_len = len(a)
        b_len = len(b)

        if b_len > a_len:
            b, a = a, b
            a_len, b_len = b_len, a_len

        res = ''
        quotient = 0
        remainder = 0

        for i in range(a_len):
            if i < b_len:
                sum_ = int(a[i]) + int(b[i]) + quotient
            else:
                sum_ = int(a[i]) + quotient
            quotient = sum_ // 2
            remainder = sum_ % 2

            res = res + str(remainder)
        
        if quotient != 0:
            res = res + '1'

        return res[::-1]


if __name__ == '__main__':
    sol = Solution()
    a = '1'
    b = '111'
    print(sol.addBinary(a, b))
