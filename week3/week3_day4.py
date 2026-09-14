# 第 3 周 Day 4 练习：面向对象入门（类与对象）
#
# C 里我们用「结构体 + 一组函数」组织数据，比如：
#     struct Student { char name[20]; ... };
#     float average(struct Student *s) { ... }
# Python 用「类」把数据和操作它的函数打包在一起，数据叫「属性」，函数叫「方法」。
#
# 运行：python week3_day4.py


# ---------- 练习 1：写一个 Student 类（跟着注释补全 TODO）----------
class Student:
    def __init__(self, name):
        """构造方法：创建对象时自动执行。

        要求：
        - 把参数 name 保存到 self.name
        - 把 self.scores 初始化成一个空列表
        """
        # TODO
        self.name=name
        self.scores=[]

    def add_score(self, score):
        """把一次成绩加入成绩列表。"""
        # TODO
        self.scores.append(score)

    
    def average(self):
        """返回平均分；如果还没有成绩，返回 0。
        """
        # TODO
        if len(self.scores)==0:
            return 0
        else:
            return sum(self.scores)/len(self.scores)

    def __str__(self):
        """print(对象) 时显示的内容。

        要求：返回类似 "Student(小明, 平均分 85.0)" 的字符串。
        """
        # TODO
        return f"Student({self.name}, 平均分 {self.average():.1f})"


# ---------- 练习 2：自己独立写一个 Rectangle 类 ----------
# 要求：
# - __init__(self, width, height) 保存长和宽到 self.width / self.height
# - area() 返回面积
# - perimeter() 返回周长
# - __str__ 返回类似 "Rectangle(3x4, 面积 12)"
class Rectangle:
    # TODO: 自己写
    def __init__(self,width,height):
        self.width=width
        self.height=height


    def area(self):
        return self.height*self.width

    def perimeter(self):
        return self.height*2+self.width*2

    def __str__(self):
        return f"Rectangle({self.width}x{self.height}, 面积 {self.area()})"

# ---------- 测试（不要改）----------
if __name__ == "__main__":
    s = Student("小明")
    s.add_score(90)
    s.add_score(80)
    s.add_score(85)

    print(s.name)          # 期望 小明
    print(s.average())     # 期望 85.0
    print(s)               # 期望 Student(小明, 平均分 85.0)

    r = Rectangle(3, 4)
    print(r.area())        # 期望 12
    print(r.perimeter())   # 期望 14
    print(r)               # 期望 Rectangle(3x4, 面积 12)
