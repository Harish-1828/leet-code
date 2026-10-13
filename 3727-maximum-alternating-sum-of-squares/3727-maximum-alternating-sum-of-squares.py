class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort(reverse=True)
        print(nums)
        mid=(len(nums)+1)//2
        print(mid)
        ans=0
        for i in range(len(nums)):
            if i<mid:
                ans+=(nums[i])
            else:
                ans-=(nums[i])
        return ans