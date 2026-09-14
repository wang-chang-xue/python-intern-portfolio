text = "hello world"
count = {}

for ch in text:
    if ch == " ":
        continue
    if ch in count:
        count[ch]=count[ch]+1
    else:
        count[ch]=1           # 跳过空格
    # TODO：如果 ch 已经在 count 里，就加 1；否则把 count[ch] 设成 1

print(count)