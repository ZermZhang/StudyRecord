from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ans = sorted(zip(ages, scores))
        dp = [i[1] for i in ans]

        for i in range(1, len(ans)):
            for j in range(i):
                if ans[i][1] >= ans[j][1]:
                    dp[i] = max(dp[i], dp[j]+ans[i][1])

        return max(dp)


if __name__ == '__main__':
    scores = [1, 3, 5, 10, 15]
    ages = [1, 2, 3, 4, 5]

    sol = Solution()
    print(sol.bestTeamScore(scores, ages))
