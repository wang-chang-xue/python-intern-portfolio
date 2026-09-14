# LeetCode 217. 存在重复元素（提交版）
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)




a=Solution().containsDuplicate([1,2,3,1])
b=Solution().containsDuplicate([1,2,3,4])
c=Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(a)
print(b)
print(c)
