class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        st=nums.index(target)
        min_v=float('inf')
        for i in range(st,len(nums)):
            if nums[i]==target and min_v> abs(i-start):
                min_v=abs(i-start)
        return min_v
        
        