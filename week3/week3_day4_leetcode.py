class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stock=[]
        for ch in s:
            if ch in pairs.values():
                stock.insert(0,ch)
            else:
                if len(stock)==0:
                    return False
                if  pairs[ch]!=stock[0]:
                    return False
                else:
                    stock.pop(0)
        if len(stock)==0:
            return True
        else:
            return False


s = "()[]{}"
print(Solution().isValid(s))
a = "])"
print(Solution().isValid(a))