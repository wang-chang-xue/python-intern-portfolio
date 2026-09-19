import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.lower()
        s3=re.sub(r"\_","",s1)
        s2=re.sub(r"[^\d\w]","",s3)
        for i in range(len(s2)//2):
            if s2[i]!=s2[len(s2)-i-1]:
                return False
        return True



if __name__=="__main__":
    s = "ab_a"
    print(Solution().isPalindrome(s))
    a = " "
    print(Solution().isPalindrome(a))
    b="A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(b))
    s = "race a car"
    print(Solution().isPalindrome(s))