def word_stats(text):
    """返回 (不同单词数, 出现最多的单词, 出现次数)"""
    # 提示：split 拆词 → set 求不同单词数 → 字典计数 → max 取最多
    num=text.split(" ")
    b=set(num)
    #print(len(b))
    count={}
    for a in num:
        count[a]=count.get(a,0)+1
    #print(max(count,key=count.get))
    return len(b),max(count,key=count.get),max(count.values())


text = "the quick brown fox jumps over the lazy dog the fox"
print(word_stats(text))     # 期望 (8, 'the', 3)



s1 = "i like python"
s2 = "i like java"
# 1. 共同单词（交集）
# 2. 只出现在 s1、只出现在 s2 的单词（差集）
count1=set(s1.split(" "))
count2=set(s2.split(" "))
print(count1&count2)
print(count1-count2)
