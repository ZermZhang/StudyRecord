from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # 从0开始，每一步都要跳的做够多
        # 如果这一步跳过的所有ele中，包含能够直接跳到尾部的长度即可
        idx, new_idx, step = 0, 0, 0

        for i in range(len(nums) - 1):
            new_idx = max(new_idx, i + nums[i])
            if idx == i:
                idx = new_idx
                step += 1
        return step

    def jump_v2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        # dp[i]记录调到nums[i]最少需要多少步
        dp = [0] * len(nums)

        # j记录从nums[j]是否能一步跳到nums[i]
        j = 0
        # 针对nums中的每个数字进行遍历
        for i in range(1, len(nums)):
            # 判断nums[j]是否能一步跳到nums[i]
            while j + nums[j] < i:
                # 如果不能的话，j前进一步
                j += 1
            # 如果能的话，代码dp[i]是从dp[j]的基础上+1 step即可实现
            dp[i] = dp[j] + 1
        # 返回跳到nums[-1]需要的最小步数
        return dp[-1]
        # if len(nums) == 1:
        #     return 1
        # if nums[idx] >= len(nums) - 1:
        #     return 1

        # while idx < len(nums):
        #     if idx + nums[idx] >= len(nums) - 1:
        #         return step
        #     new_idx = idx + nums[idx]
        #     print(idx, new_idx)
        #     for j in range(idx + 1, idx + nums[idx]):
        #         print('\t\t', j, idx + j + nums[j])
        #         if new_idx > idx + j + nums[j]:
        #             continue
        #         else:
        #             new_idx = idx + j + nums[j]
        #     idx = new_idx
        #     step = step + 1
        #     print('\t', idx, step)


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 1, 1, 1]
    # nums = [2, 3, 1, 1, 4]
    # nums = [1, 1, 1, 1, 1]  # 4
    nums = [3, 4, 3, 2, 5, 4, 3]  # 3

    print(sol.jump_v2(nums=nums))
