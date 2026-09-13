class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        row=len(grid)
        col=len(grid[0])
        def dfs(st):
            row=len(grid)
            col=len(grid[0])
            stack=[]
            stack.append(st)
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            visited.add((st[0],st[1]))
            while stack:
                x,y=stack.pop()
                for i,j in directions:
                    if ((i+x)>=0 and (i+x)<row) and ((j+y)>=0 and (j+y)<col) and ((i+x,y+j) not in visited) and (grid[i+x][y+j]=='1'):
                        visited.add((i+x,y+j))
                        stack.append((i+x,y+j))
        cnt=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and (i,j) not in visited:
                    cnt+=1
                    dfs((i,j))
        return cnt


        