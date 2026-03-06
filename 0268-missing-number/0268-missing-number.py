class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        list1=[i for i in range(len(nums)+1)]
        s1=set(nums)
        s2=set(list1)
        print(s1)
        print(s2)
        s=s2-s1
        
        return next(iter(s))