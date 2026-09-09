def two_sum(nums, target):
    # 用双层循环找两个数，它们的和等于 target
    # 找到就返回 [i, j]
    pass
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


# 下面两行是测试，不要改：
print(two_sum([2, 7, 11, 15], 9))   # 应输出 [0, 1]，因为 2+7=9
print(two_sum([3, 2, 4], 6))        # 应输出 [1, 2]，因为 2+4=6