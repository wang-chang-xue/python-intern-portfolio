# 项目 1（v1）：单词频率分析器
#
# 目标：统计一段文本的「总词数 / 不同单词数 / 出现最多的前 5 个单词」
#
# 运行方式（VS Code 终端）：
#   conda activate intern
#   python project1_word_freq.py
#
# 说明：先把下面两个 TODO 函数实现，再运行 main。实现前运行会报错，属正常。

SAMPLE_TEXT = (
    "The quick brown fox jumps over the lazy dog. "
    "The dog barks, and the fox runs away. "
    "A quick brown dog jumps over a lazy fox."
)


def analyze(text):
    """统计每个单词出现的次数。

    要求：
    - 全部转成小写（lower）
    - 去掉常见标点（.,!? 等，可用 replace 逐个替换成空字符串）
    - 用 split() 按空白拆分成单词

    返回：
    - 字典 {单词: 次数}
    """
    # TODO: 实现这个函数
    text=text.replace("."," ").replace(","," ").replace("?"," ").replace("!"," ")
    count1=text.lower().split()
    count={}
    for i in count1:
        count[i]=count.get(i,0)+1
    return count








def top_words(count, n=5):
    """返回出现次数最多的前 n 个 (单词, 次数)。

    参数：
    - count：analyze() 返回的字典
    - n：取前几个

    返回：
    - 列表，如 [('the', 4), ('dog', 3), ...]

    提示（用你已经会的方法即可）：
    - 复制一份字典 temp = dict(count)
    - 循环 n 次：用 max(temp, key=temp.get) 取出当前次数最多的单词，
      把 (单词, 次数) 加进结果列表，然后 del temp[单词]
    （更简洁的 sorted + lambda 写法会在第 3 周学到）
    """
    # TODO: 实现这个函数
    temp=dict(count)
    result=[]
    for i in range(min(n,len(count))):
        best = max(temp, key=temp.get)
        result.append((best, temp[best]))
        del temp[best]
    return result




def main():
    count = analyze(SAMPLE_TEXT)

    print("总词数：", sum(count.values()))
    print("不同单词数：", len(count))
    print("出现最多的前 5 个单词：")
    for word, times in top_words(count, 5):
        print(f"  {word}: {times}")


if __name__ == "__main__":
    main()
