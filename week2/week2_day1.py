# 第 2 周 Day 1 练习：输入、运算与比较
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))

c = a + b
print("两个数的和为：", c)

if a > b:
    print("第一个数大于第二个数")
elif a < b:
    print("第一个数小于第二个数")
else:
    print("两个数相等")
