# 项目 1（v3）：模块化版本
# 功能函数都写在 wordfreq_tools.py 里，这个脚本只负责「导入并使用」。
#
# 运行：
#   python project1_word_freq_v3.py                # 默认读 sample.txt
#   python project1_word_freq_v3.py 别的文件.txt

import sys

from wordfreq_tools import analyze, load_text, top_words


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
