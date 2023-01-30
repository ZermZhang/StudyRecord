class Solution:
    def tribonacci(self, n: int) -> int:
        # 传统方法，性能较差。39.1% runtime, 54.1% memory
        t = []
        t.extend([0, 1, 1])

        # 逐步计算tribonacci序列
        for i in range(3, n):
            tmp = t[i-1] + t[i-2] + t[i-3]
            t.append(tmp)

        t.append(t[n-1] + t[n-2] + t[n-3])

        # 输出最后需要使用到的值
        return t[n]

    def tribonacci_v2(self, n: int) -> int:
        # 会出现运行超时的问题
        t = [0, 1, 1]

        if n < 3:
            return t[n]
        else:
            return self.tribonacci_v2(n - 1) + self.tribonacci_v2(n - 2) + self.tribonacci_v2(n - 3)


if __name__ == '__main__':
    sol = Solution()
    n = 25

    print(sol.tribonacci(n))
    print(sol.tribonacci_v2(n))
