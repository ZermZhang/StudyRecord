from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = 0
        while n < len(nums) - 1:
            if nums[n] == nums[n+1]:
                n = n + 2
            else:
                return nums[n]
        return nums[len(nums) - 1]

    def singleNonDuplicate_base(self, nums: List[int]) -> int:
        res = {}

        for ele in nums:
            res[ele] = res.get(ele, 0) + 1
        
        res = sorted(res.items(), key=lambda ele: ele[1], reverse=False)
        return res[0][0]

if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,2,3,3,4,4,8,8]
    nums = [3,3,7,7,10,11,11]
    print(sol.singleNonDuplicate(nums))
