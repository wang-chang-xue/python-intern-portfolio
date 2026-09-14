class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        count={}
        for i in strs:
            key="".join(sorted(i))
            if key in count:
                count[key].append(i)
            else:
                count[key]=[]
                count[key].append(i)
        return list(count.values())



    def majorityElement(self, nums: list[int]) -> int:
        return sorted(nums)[len(nums) // 2]


a=Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(a)
nums = [2,2,1,1,1,2,2]
b=Solution().majorityElement(nums)
print(b)


    
     

