class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s2={i for i in range(len(nums)+1)}
        s1=set(nums)
        s=s2-s1
        return next(iter(s))