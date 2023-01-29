# ==================================================
#   6. Zigzag Conversion
#   Input: s = "PAYPALISHIRING", numRows = 4
#   Output: "PINALSIGYAHRPI"
#   Explanation:
#   P     I    N
#   A   L S  I G
#   Y A   H R
#   P     I
#
# ==================================================

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 对numRows为1的情况，可以直接返回，方便处理
        if numRows == 1:
            return s

        # 更具具体的行数情况记录需要额外处理的信息
        zig_list = [''] * numRows
        # 记录当前正在处理的是哪个序列的信息
        row_idx = 0
        # 记录指针需要超哪个方向走，默认是从左边开始朝右边走
        step = 1

        # 开始遍历整个字符串
        for ele in s:
            # 将当前的字符串写入到指定的待处理序列里
            zig_list[row_idx] += ele
            # 调整行走方向
            if row_idx == numRows - 1:
                step = -1
            if row_idx == 0:
                step = 1
            # 指针朝指定方向走一步
            row_idx = row_idx + step

        return ''.join(zig_list)


if __name__ == '__main__':
    sol = Solution()
    s = 'PAYPALISHIRING'
    numRows = 4

    print(sol.convert_v2(s, numRows))
