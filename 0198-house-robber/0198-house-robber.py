class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)-1
 
        dp={}
        def fn(n):
            if n >= len(nums):
                return 0
            if n in dp:
                return dp[n]
            dp[n]=max(nums[n]+fn(n+2),fn(n+1))
            return dp[n]
        return fn(0)