class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n=0
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
                n+=1
            else:
                digits[i]=digits[i]+1
                break
        if n == len(digits):
            digits[0]=1
            digits.append(0)

        return digits
        


digits = [4,3,2,1]
print(Solution().plusOne(digits))
digits = [9,9,9,9]
print(Solution().plusOne(digits))