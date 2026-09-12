# 第 3 周 Day 1 练习：文件读写 + 异常处理
#
# 今天的三个练习都在这个文件里，写完直接运行：
#   conda activate intern
#   python week3_day1.py
#
# C ↔ Python 对照（先读一遍再动手）：
# - C 里用 fopen/fclose 手动开关文件；Python 用 `with open(...) as f:`，
#   离开 with 这一段代码块时文件会自动关闭，不需要手动 fclose。
# - C 里读写要指定类型和长度；Python 的 f.write() 只收字符串，
#   要写数字先 str() 转换。
# - C 里靠函数返回值判断出错；Python 用 try/except 接住异常。
#
# 说明：三个 TODO 都实现完再运行；实现前运行会报错，属正常。

import os

#NOTE_FILE = "E:/python文件/week3_note.txt"
NOTE_FILE = "week3_note.txt"

#os.makedirs(NOTE_FILE, exist_ok=True)


def write_note(path, lines):
    """把 lines 里的每一行写进文件，每行末尾补一个换行符。

    要求：
    - 用 with open(path, "w", encoding="utf-8") as f
    - 对 lines 里每一行执行 f.write(line + "\n")
    - 不需要 return
    """
    # TODO: 实现这个函数
    #line=lines.spilt("\n")
    with open(path,"w",encoding="utf-8") as f:
        for line in lines:
            f.write(line+"\n")


    


def read_note(path):
    """读回文件内容，返回「行列表」，每行不含末尾换行。

    提示（两种写法都行，选一种）：
    - f.readlines() 得到带 "\n" 的行列表，再用 line.strip() 去掉换行
    - 或者 f.read().splitlines() 直接得到去掉换行的行列表
    """
    # TODO: 实现这个函数
    with open(path,"r",encoding="utf-8") as f:
        return f.read().splitlines()


def to_int(s):
    """把字符串转成整数；转不了就返回 None。

    要求：
    - 用 try / except ValueError，不要用 s.isdigit() 之类的预判断
    - 例如 to_int("42") -> 42，to_int("abc") -> None
    """
    # TODO: 实现这个函数
    try:
        s=int(s)
        return s
    except ValueError:
        return None


def main():
    # 练习 A：写文件
    write_note(NOTE_FILE, ["Python 第 3 周", "文件读写练习", "异常处理练习"])

    # 练习 B：读文件
    lines = read_note(NOTE_FILE)
    print("文件里一共有", len(lines), "行：")
    for line in lines:
        print("  -", line)

    # 练习 C：异常处理
    for s in ["42", "3.14", "abc", ""]:
        print(f"to_int({s!r}) ->", to_int(s))

    # 收尾：删掉练习用的临时文件（删文件也要处理「文件不存在」）
    try:
        os.remove(NOTE_FILE)
        print("已删除", NOTE_FILE)
    except FileNotFoundError:
        print(NOTE_FILE, "不存在，无需删除")


if __name__ == "__main__":
    main()
