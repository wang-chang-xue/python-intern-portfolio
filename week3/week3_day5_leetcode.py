class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        count=10000
        s=0
        for i in prices:
            if i < count:
                count=i
            if i > count:
                s=max(s,i-count)
        return s



if __name__ == "__main__":
    a=[7,1,5,3,6,4]
    print(Solution().maxProfit(a))