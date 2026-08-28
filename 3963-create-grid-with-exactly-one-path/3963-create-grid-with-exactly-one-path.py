class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[['*'] * n for _ in range(m)]
        res=[]
        for i in range(m):
            for j in range(n):
                if i==0:
                    grid[i][j]="."
                elif i!=0 and j==n-1:
                    grid[i][j]="."
                else:
                    grid[i][j]="#"
            res.append(''.join(grid[i]))
        return res
            

            
        