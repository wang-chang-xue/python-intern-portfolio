# LeetCode 136. 只出现一次的数字（提交版）
# 本地运行前记得保留这一行，网页模板自带；少了会报 NameError: name 'List' is not defined
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """数组里除某个元素只出现一次外，其余都出现两次，找出那个元素。

        两种写法都试一下：
        1. 先用你已经会的字典计数：统计每个数字出现次数，返回次数为 1 的那个。
        2. 再想一个更妙的：异或（^）满足 a ^ a = 0、a ^ 0 = a、且可交换，
           把所有数字异或一遍，成对的会互相抵消，剩下的就是答案（空间 O(1)）。
        """
        # 另一种写法（字典计数）：
        # count = {}
        # for i in nums:
        #     count[i] = count.get(i, 0) + 1
        # for j in count:
        #     if count[j] == 1:
        #         return j
        result=0
        for i in nums:
            result^=i
        return result
            
            





if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 1]))        # 1
    print(Solution().singleNumber([4, 1, 2, 1, 2]))  # 4
    print(Solution().singleNumber([1]))              # 1
