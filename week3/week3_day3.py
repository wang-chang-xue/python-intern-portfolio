# 第 3 周 Day 3 练习：lambda / sorted / map / filter + 模块
#
# 运行：python week3_day3.py
# 每道题下面都有期望输出，做完对照一下。

import math
import random


# ---------- 练习 1：sorted + key ----------
nums = [5, 2, 9, 1, 7]
words = ["banana", "apple", "cherry", "fig"]

# 1a. 把 nums 升序排序（用 sorted，不要改原列表）
# TODO
nums_sorted = None
nums_sorted=sorted(nums)
print("1a:", nums_sorted)          # 期望 [1, 2, 5, 7, 9]

# 1b. 把 words 按「单词长度」升序排序
# 提示：sorted(words, key=len)
# TODO
words_by_len = None
words_by_len=sorted(words,key=len)
print("1b:", words_by_len)         # 期望 ['fig', 'apple', 'banana', 'cherry']

# 1c. 把 words 按「最后一个字母」升序排序（用 lambda）
# 提示：key=lambda w: w[-1]
# TODO
words_by_last = None
words_by_last=sorted(words,key=lambda w:w[-1])
print("1c:", words_by_last)


# ---------- 练习 2：按字典的值排序 ----------
count = {"the": 4, "fox": 3, "dog": 3, "quick": 2, "brown": 2}

# 2a. 用 sorted + lambda 得到按次数降序的 (单词, 次数) 列表
# 提示：count.items() 得到 (键, 值) 的序列，key=lambda x: x[1]
# TODO
ranked = None
ranked=count.items()
ranked=sorted(ranked,key=lambda w:w[1],reverse=True)
print("2a:", ranked)               # 期望 [('the', 4), ('fox', 3), ('dog', 3), ('quick', 2), ('brown', 2)]


# ---------- 练习 3：map / filter（能读懂即可）----------
# 3a. 用 map + lambda 把 nums 每个数翻倍
# TODO
doubled = None
doubled=[2*n for n in nums]
doubled=list(map(lambda n:2*n,nums))
print("3a:", doubled)              # 期望 [10, 4, 18, 2, 14]

# 3b. 用 filter + lambda 取出 nums 里的偶数
# TODO
evens = None
evens=[n for n in nums if n%2==0]
evens=list(filter(lambda n:n%2 ==0,nums))
print("3b:", evens)                # 期望 [2]


# ---------- 练习 4：使用标准库模块 ----------
# 4a. 用 math.sqrt 计算 2027 的平方根，结果保留 2 位小数
# TODO
root = None
root=round(math.sqrt(2027),2)
print("4a:", root)                 # 期望 45.02

# 4b. 用 random.randint 生成一个 1~100 的随机整数
# TODO
r = None
r=random.randint(1,100)
print("4b:", r)                    # 每次运行都不同，1~100 之间
