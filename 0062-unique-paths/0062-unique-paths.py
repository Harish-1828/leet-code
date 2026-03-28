class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = {}  

        def start(x, y):
            if x == m - 1 or y == n - 1:
                return 1
            
            if (x, y) in dp:  
                return dp[(x, y)]
            
            dp[(x, y)] = start(x + 1, y) + start(x, y + 1)
            return dp[(x, y)]

        return start(0, 0)