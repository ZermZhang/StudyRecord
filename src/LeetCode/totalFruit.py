from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(set(fruits)) == 1:
            return len(fruits)

        former = 0
        laster = 1

        total_cnt = 0

        while laster < len(fruits):
            print(former, laster, total_cnt)
            if len(set(fruits[former: laster + 1])) <= 2:
                total_cnt = max(total_cnt, len(fruits[former: laster + 1]))
                print('\t', total_cnt)
            else:
                former = former + 1
            laster += 1

        return total_cnt

    def totalFruit_v2(self, fruits: List[int]) -> int:
        left = 0
        buckets = {}

        # 遍历所有的果树
        for right, fruit in enumerate(fruits):
            # 将当前果树的类型加入大bucket中进行记录
            buckets[fruit] = buckets.get(fruit, 0) + 1

            # 检查bucket中有多少种type
            if len(buckets) > 2:
                # 如果超过2种的话，对最左边的type减1
                buckets[fruits[left]] -= 1

                # 如果最左边的类型被全部删除了，左边指针进位
                if buckets[fruits[left]] == 0:
                    del buckets[fruits[left]]
                left += 1
        # 注意，这里到最后，有可能buckets依旧超过两种
        # 原因是，虽然前面的type在逐步删除，但是每删除一个left，right同时进了一位，相当于是位置互换，但是数量不变
        print(buckets)

        return right - left + 1


if __name__ == '__main__':
    sol = Solution()
    fruits = [0, 0, 0, 0, 0, 1, 2]
    print(sol.totalFruit_v2(fruits=fruits))
