class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        idx=nums.index(max(nums))
        s=0
        for i in range(k):
            s=s+nums[idx]
            nums[idx]+=1
        return s