class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)-1
        dp=defaultdict(int)
        d={}
        for idx,i in enumerate(cost):
            dp[idx]=i
        def fn(n):
            if n==len(cost)-2 or n==len(cost)-1:
                return dp[n]
            if n in d:
                return d[n]
            left=fn(n+1)
            right=fn(n+2)
            d[n]=dp[n]+min(left,right)
            return d[n]
        return min(fn(0),fn(1))