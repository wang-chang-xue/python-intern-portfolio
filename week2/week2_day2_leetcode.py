# LeetCode 1. 两数之和（Two Sum）— Python3 提交版
#
# 使用方法：
# 1. 打开 leetcode.cn 的「两数之和」题目，语言选 Python3；
# 2. 把下面 class Solution 一整段复制进编辑器（覆盖模板内容），点「提交」；
# 3. 本地想先跑一遍，直接运行本文件即可。

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []   # 题目保证有唯一解，这行实际不会执行，写上更稳妥


# ---------------- 本地测试（提交时不要复制这部分）----------------
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))   # 期望 [0, 1]
    print(s.twoSum([3, 2, 4], 6))        # 期望 [1, 2]
