# 第 2 周 Day 2 练习：两数之和（本地函数版）


def two_sum(nums, target):
    # 用双层循环找出两个数，它们的和等于 target
    # 找到就返回 [i, j]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(two_sum([2, 7, 11, 15], 9))   # 期望 [0, 1]，因为 2+7=9
print(two_sum([3, 2, 4], 6))        # 期望 [1, 2]，因为 2+4=6
