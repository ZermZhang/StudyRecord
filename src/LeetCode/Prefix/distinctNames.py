from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # 最普通的方法，可以输出，但是因为时间复杂度是O(n^2)，所以遇到了较长的序列之后容易超时
        length = len(ideas)
        count = 0

        for i in range(length):
            for j in range(i + 1, length):
                idea_a = ideas[i]
                idea_b = ideas[j]

                idea_a_s = idea_b[0] + idea_a[1:]
                idea_b_s = idea_a[0] + idea_b[1:]

                print(idea_a, idea_b, idea_a_s, idea_b_s, idea_a_s in ideas, idea_b_s in ideas)
                if idea_a_s in ideas or idea_b_s in ideas:
                    continue
                else:
                    count += 1
        return count * 2

    def distinctNames_v3(self, ideas: List[str]) -> int:
        from collections import defaultdict

        # 统计左右的idea的首字母分布情况，并记录
        # 注意这里记录的是除了首字母之外的idea剩下的部分
        dct = defaultdict(set)
        for idea in ideas:
            dct[idea[0]].add(idea[1:])

        arr = list(dct.keys())

        count = 0
        # 对所有可能首字母进行双向遍历
        for i in range(len(dct)):
            for j in range(i + 1, len(dct)):
                count += (
                    # 注意这里的操作，两个set， A - B，会保留A里面存在但是B里不存在的元素
                    # 即dct[arr[i]] - dct[arr[j]]，会保留arr[i](首字母) + dct[arr[j]]（后缀）不属于idea中的值
                    len(dct[arr[i]] - dct[arr[j]]) * len(dct[arr[j]] - dct[arr[i]]) * 2
                )
        return count

    def distinctNames_v2(self, ideas: List[str]) -> int:
        # 核心在于：
        # 0. 需要两两配对
        # 1. 每个词首字母替换了所有可能的首字母后是否出现在ideas中
        # 2. 组成的公司名是否可能会出现重复，出现重复的会需要去重
        # 虽然每次的迭代长度短了，但是依旧会出现超时的情况
        # 但是通过字典降低检索时间的方法应该是可行的
        head_alphas_dict = {}
        for idea in ideas:
            alpha = idea[0]
            if alpha not in head_alphas_dict:
                head_alphas_dict[alpha] = [idea]
            else:
                head_alphas_dict[alpha].append(idea)

        print(head_alphas_dict)
        valid_names = []
        for idea in ideas:
            for alpha, alpha_ideas in head_alphas_dict.items():
                if alpha == idea[0]:
                    continue
                else:
                    idea_a = alpha + idea[1:]
                    if idea_a in alpha_ideas:
                        continue
                    else:
                        for alpha_idea in alpha_ideas:
                            idea_b = idea[0] + alpha_idea[1:]
                            if idea_b in head_alphas_dict[idea[0]]:
                                continue
                            else:
                                valid_names.append(idea_a + idea_b)

        return len(valid_names)


if __name__ == '__main__':
    sol = Solution()
    # ideas = ["coffee", "donuts", "time", "toffee"]   # 6
    # ideas = ['lack', 'back']  # 0
    ideas = ["aaa","baa","caa","bbb","cbb","dbb"]   # 2
    print(sol.distinctNames_v3(ideas=ideas))
