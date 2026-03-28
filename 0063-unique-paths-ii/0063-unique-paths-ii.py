class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]==1:
            return 0
        dp={}
        def start(x,y):
            if x>=m or y>=n:
                return 0
            if  obstacleGrid[x][y]==1:
                return 0
            if (x,y) in dp:
                return dp[(x,y)]
            if x==m-1 and y==n-1:
                return 1
            else:
                dp[(x,y)]=start(x+1,y)+start(x,y+1)
                return dp[(x,y)]
        return start(0,0)