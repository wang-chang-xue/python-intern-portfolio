text = "the quick brown fox jumps over the lazy dog the fox"

# 1. 用 split() 拆成单词列表
# 2. 用 set 统计有多少个不同的单词
# 3. 用字典统计每个单词出现次数，找出出现最多的单词

class Solution():
    def sp(self, s:str):
        num=s.split(" ")
        b=set(num)
        print(b)
        print(len(b))
        count={}
        for a in num:
            count[a]=count.get(a,0)+1
        return max(count,key=count.get)

a=Solution().sp(text)
print(a)