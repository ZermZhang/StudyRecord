from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # 将年龄和得分组合后按照年龄升序进行排序
        ans = sorted(zip(ages, scores))
        # 保留按照年龄升序的得分序列
        # dp = [i[1] for i in ans]

        # for i in range(1, len(ans)):
        #     for j in range(i):
        #         # 如果当前得分大于前面的得分，则进行累加
        #         if ans[i][1] >= ans[j][1]:
        #             dp[i] = max(dp[i], dp[j]+ans[i][1])
        res = self.MaxSumInList([ele[1] for ele in ans])

        return max(res)

    def MaxSumInList(self, llist: List[int]) -> List[int]:
        # 获取List中和最大的升序子序列
        res = [ele for ele in llist]
        for i in range(1, len(llist)):
            for j in range(i):
                if llist[i] >= llist[j]:
                    res[i] = max(res[i], res[j] + llist[i])
        return res


if __name__ == '__main__':
    scores = [4, 5, 6, 5]
    ages = [2, 1, 2, 1]

    sol = Solution()
    print(sol.bestTeamScore(scores, ages))
