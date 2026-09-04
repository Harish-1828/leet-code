class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_idx=nums.index(min(nums))
        max_idx=nums.index(max(nums))
        back1=len(nums)-min_idx
        back2=(len(nums)-max_idx)
        print(min_idx,max_idx)
        print(back1,back2)
        res1=min(min_idx+1,back1)
        res2=min(max_idx+1,back2)
        return min(res1+res2,max(min_idx+1,max_idx+1),max(back1,back2))