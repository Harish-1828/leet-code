class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maximum=[-1]*len(nums)
        maximum[0]=nums[0]
        minimum=[-1]*len(nums)
        minimum[-1]=nums[-1]
        for i in range(1,len(nums)):
            maximum[i]=max(maximum[i-1],nums[i])
        for i in range(len(nums)-2,-1,-1):
            minimum[i]=min(minimum[i+1],nums[i])
        for i in range(len(nums)):
            s=maximum[i]-minimum[i]
            if s<=k:
                return i
        return -1
  
