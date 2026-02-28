class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                left=float('inf')
                up=float('inf')
                if i!=0:
                   up =grid[i-1][j]+grid[i][j]
                if j!=0:
                    left=grid[i][j-1]+grid[i][j]
                grid[i][j]=min(up,left)
        return grid[m-1][n-1]