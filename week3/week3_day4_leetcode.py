class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stock=[]
        for ch in s:
            if ch in "({[":
                stock.append(ch)
            else:
                if len(stock)==0:
                    return False
                if  pairs[ch]!=stock[-1]:
                    return False
                else:
                    stock.pop()
        return len(stock)==0


s = "()[]{}"
print(Solution().isValid(s))
a = "])"
print(Solution().isValid(a))