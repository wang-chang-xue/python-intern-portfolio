import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_log(path):
    try:
        with open(path,"r",encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return  None


def parse_line(line):
    read=re.match(r"^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) ([A-Z]+) (.+)$",line)
    if read:
        return read.groups()
    else:
        return None


def count_levels(lines):
    counts={}
    for i in lines:
        m1=parse_line(i)
        if m1:
            m=m1[2]
            counts[m]=counts.get(m,0)+1
    return counts
        
if __name__ == "__main__":
    lines = load_log(os.path.join(BASE_DIR, "sample.log"))
    if not lines:
        print("找不到文件：sample.log")
    else:
        print("总行数：", len(lines))
        print("级别统计：")
        for level, n in count_levels(lines).items():
            print(f"  {level}: {n}")
