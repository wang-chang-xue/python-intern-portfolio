# 项目 1（v2）：单词频率分析器 —— 从文件读取 + 列表推导式
#
# 运行方式：
#   conda activate intern
#   python project1_word_freq_v2.py                # 默认读 sample.txt
#   python project1_word_freq_v2.py 别的文件.txt    # 读指定文件
#
# 与 v1 的区别：
# 1. 文本来自外部文件，而不是写死在代码里
# 2. 用列表推导式清洗单词（去标点 + 转小写）
# 3. 文件不存在时用 try/except 友好提示，而不是直接崩溃

import sys


def load_text(path):
    """读文件并返回全部文本；文件不存在则返回 None。

    要求：
    - 用 with open(path, "r", encoding="utf-8") as f
    - 用 try / except FileNotFoundError 捕获「文件不存在」
    """
    # TODO: 实现
    
    try:
        with open(path,"r",encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None



def analyze(text):
    """统计每个单词出现的次数（本版本要求用列表推导式清洗）。

    要求：
    1. 用列表推导式把 text.split() 里的每个词去掉首尾标点并转小写：
       提示：w.strip(".,!?;:") 去掉首尾这些符号，再 .lower()
    2. 再用一个列表推导式过滤掉空字符串（比如整词都是标点的情况）
    3. 用字典统计词频，返回 {单词: 次数}

    示例：
        text = "The dog. The cat!"
        -> {'the': 2, 'dog': 1, 'cat': 1}
    """
    s=text.split()
    cleaned=[w.strip(".,?!;:").lower() for w in s]
    nonempty=[w for w in cleaned if w]
    count={}
    for i in nonempty:
        count[i]=count.get(i,0)+1
    return count



def top_words(count, n=5):
    """返回出现次数最多的前 n 个 (单词, 次数)。（可直接从 v1 复制）"""
    temp = dict(count)
    result = []
    for _ in range(min(n, len(count))):
        w = max(temp, key=temp.get)
        result.append((w, temp[w]))
        del temp[w]
    return result


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"

    text = load_text(path)
    if text is None:
        print(f"找不到文件：{path}")
        return

    count = analyze(text)

    print(f"文件：{path}")
    print("总词数：", sum(count.values()))
    print("不同单词数：", len(count))
    print("出现最多的前 5 个单词：")
    for word, times in top_words(count, 5):
        print(f"  {word}: {times}")


if __name__ == "__main__":
    main()
