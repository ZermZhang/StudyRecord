class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + max(low % 2, high % 2)


if __name__ == '__main__':
    sol = Solution()
    low = 14
    high = 17
    print(sol.countOdds(low, high))
