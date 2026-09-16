from datetime import datetime, timedelta
import json


def days_between(d1, d2):
    day1=datetime.strptime(d1,"%Y-%m-%d")
    day2=datetime.strptime(d2,"%Y-%m-%d")
    subtract=max(day1,day2)-min(day1,day2)
    return subtract.days


def add_days(date_str, n):
    d=datetime.strptime(date_str,"%Y-%m-%d")
    return (d+timedelta(days=n)).strftime("%Y-%m-%d")


def to_json(data):
    return json.dumps(data,ensure_ascii=False,indent=2)


def from_json(s):
    return json.loads(s)


def save_json(path, data):
    with open(path,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)


def load_json(path):
    with open(path,"r",encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    print(days_between("2026-09-01", "2026-09-16"))
    print(add_days("2026-09-16", 7))

    data = {"name": "小明", "scores": [90, 85]}
    s = to_json(data)
    print(s)
    print(from_json(s)["name"])

    save_json("week4_demo.json", data)
    print(load_json("week4_demo.json")["scores"])
