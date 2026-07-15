class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def fn(i):
            if i <= 1:
                return i

            if dp[i] != -1:
                return dp[i]

            dp[i] = fn(i - 1) + fn(i - 2)
            return dp[i]

        return fn(n)