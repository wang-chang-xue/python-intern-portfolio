# 项目 1 的功能模块：单词频率分析的核心函数放在这里，供其他脚本 import 使用。
# 这就是「模块化」：功能写一份，多个脚本都能复用。


def load_text(path):
    """读文件并返回全部文本；文件不存在则返回 None。"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None


def analyze(text):
    """用列表推导式清洗文本，再统计词频，返回 {单词: 次数}。"""
    words = [w.strip(".,!?;:").lower() for w in text.split()]
    words = [w for w in words if w]

    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1
    return count


def top_words(count, n=5):
    """返回出现次数最多的前 n 个 (单词, 次数)。

    Day 3 重点：用 sorted + lambda 一行搞定，不要再写「循环 + max」。

    提示：sorted(count.items(), key=lambda x: x[1], reverse=True)[:n]
    """
    # TODO: 用 sorted + lambda 实现
    return sorted(count.items(),key=lambda w:w[1],reverse=True)[:n]
