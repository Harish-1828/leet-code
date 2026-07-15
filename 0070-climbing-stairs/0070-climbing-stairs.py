class Solution:
    def climbStairs(self, n: int) -> int:
        dp={0:1,1:1}
        def fn(n):
            if n in dp:
                return dp[n]
            dp[n]=fn(n-1)+fn(n-2)
            return dp[n]
        return fn(n)
        