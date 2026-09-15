class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        count=10000
        sum=0
        for i in prices:
            if i < count:
                count=i
            if i > count:
                sum=max(sum,i-count)
        return sum

    
a=[7,1,5,3,6,4]
print(Solution().maxProfit(a))