class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left <=right:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            if nums[mid]<target:
                left=mid+1
            if nums[mid]==target:
                return mid
        return -1
        

if __name__ == "__main__":
    n=[-1,0,3,5,9,12]
    t=9
    print(Solution().search(n,t))

