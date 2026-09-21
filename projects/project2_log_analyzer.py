import os
import re
import json
import sys
from datetime import datetime

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
        
def filter_by_time(lines, start=None, end=None):
    lists=[]
    start_date=datetime.strptime(start,"%Y-%m-%d %H:%M:%S")if start else None
    end_date=datetime.strptime(end,"%Y-%m-%d %H:%M:%S")if end else None
    for i in lines:
        parts=parse_line(i)
        if not parts:
            continue
        i_date=datetime.strptime(parts[0] + " " + parts[1],"%Y-%m-%d %H:%M:%S")
        if start_date and i_date<start_date:
            continue
        if end_date and i_date>end_date:
            continue
        lists.append(i)
    return lists


def build_report(lines):
    counts={}
    counts["total"]=len(lines)
    counts["levels"]=count_levels(lines)
    for i in lines:
        if re.match(r"\d{4}-\d{2}-\d{2}",i):
            counts["first"]=re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",i).group()
            break
    for j in reversed(lines):
        if re.match(r"\d{4}-\d{2}-\d{2}",j):
            counts["last"]=re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",j).group()
            break
    return counts


def save_report(report, path):
    with open(path,"w",encoding="utf-8")as f:
        json.dump(report,f,ensure_ascii=False,indent=2)


if __name__ == "__main__":
    lines = load_log(os.path.join(BASE_DIR, "sample.log"))
    start = sys.argv[1] if len(sys.argv) > 1 else None
    end = sys.argv[2] if len(sys.argv) > 2 else None
    if not lines:
        print("找不到文件：sample.log")
    else:
        print("总行数：", len(lines))
        print("级别统计：")
        for level, n in count_levels(lines).items():
            print(f"  {level}: {n}")

        lists=filter_by_time(lines,start,end)
        report=build_report(lists)
        print(report)
        save_report(report,os.path.join(BASE_DIR, "report.json"))
