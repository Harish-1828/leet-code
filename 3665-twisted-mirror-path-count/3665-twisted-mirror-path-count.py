class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        dp=[[-1]*len(grid[0]) for _ in range(len(grid))]
        def fn(x,y,dir):
            if y==len(grid[0])-1 and x==len(grid)-1:
                return 1
            elif x>=len(grid):
                return 0
            elif y>=len(grid[0]):
                return 0
            elif dp[x][y]!=-1:
                return dp[x][y]
            elif grid[x][y]==1:
                if dir==1:#l=right 2=down
                    path1=fn(x,y+1,2)
                else:
                    path1=fn(x+1,y,1)
                return path1
            else:
                right=fn(x+1,y,1)
                down=fn(x,y+1,2)
                dp[x][y]=(right+down)%(pow(10,9)+7)
                return dp[x][y]
        return fn(0,0,1)