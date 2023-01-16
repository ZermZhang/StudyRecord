# ------------------------
#   1813. 句子相似性 III
# ------------------------

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # 将str类型的句子split为两个数组，方便后续处理
        words1, words2 = sentence1.split(), sentence2.split()
        m, n = len(words1), len(words2)
        # 两个句子可能长度不稳定，人为处理为words1的长度大于words2的长度的情况，即 n < m
        if m < n:
            words1, words2 = words2, words1
            m, n = n, m
        # 设置两个指针
        i = j = 0

        # 从两个句子的头部开始变量相似的word
        while i < n and words1[i] == words2[i]:
            i += 1
        # 从头开始的相似子序列遍历完毕，记录头部相同的长度i

        # 从句子的尾部开始遍历相似的word
        while j < n and words1[m - 1 - j] == words2[n - 1 - j]:
            j += 1
        # 从尾部开始的相似子序列遍历完毕，记录尾部相同的长度j

        # 比较头尾相同的长度是否和n(较短的句子长度)相同
        # 如果相同，则说明较长的具体需要增加的部分都处在中间位置，可以通过插入一个句子完成转换
        # 否则不行
        return i + j >= n
