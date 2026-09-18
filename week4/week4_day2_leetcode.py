class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[n]=nums[i]
                n=1+n
        for j in range(n,len(nums)):
            nums[j]=0
                


if __name__ == "__main__":
    nums =[0,0,1]
    Solution().moveZeroes(nums)
    print(nums)