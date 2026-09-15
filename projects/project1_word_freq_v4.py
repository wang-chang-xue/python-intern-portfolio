import sys

from wordfreq_tools import analyze as an, load_text as lo

class WordAnalyzer:
    def __init__(self,path):
        self.path=path
        self.count={}

    def load_text(self):
        return lo(self.path)

    def analyze(self):
        text = self.load_text()
        if text is None:
            return False
        self.count = an(text)
        return True

    def top_words(self,n=5):
        return sorted(self.count.items(),key=lambda w:w[1],reverse=True)[:n]

    def report(self):
        if not self.analyze():
            print(f"找不到文件：{self.path}")
            return

        print(f"文件：{self.path}")
        print("总词数：",sum(self.count.values()))
        print("不同单词数：",len(self.count))
        for word,time in self.top_words(5):
            print(f"{word}:{time}")

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"

    s=WordAnalyzer(path)
    s.report()



if __name__ == "__main__":
    main()