class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)-1
        if(l==0):
            return nums[0]
        dp={}
        def fn(n,n1):
            if n >= len(n1) :
                return 0
            if n in dp:
                return dp[n]
            dp[n]=max(n1[n]+fn(n+2,n1),fn(n+1,n1))
            return dp[n]
        x1=(fn(0,nums[:-1]))
        dp={}
        x2=(fn(0,nums[1:]))
        return max(x1,x2)