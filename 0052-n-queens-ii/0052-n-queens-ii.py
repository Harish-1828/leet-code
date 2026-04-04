class Solution:
    def totalNQueens(self, n: int) -> int:
        chess=[['.']*n for i in range(n)]
        result=[0]
        def conflict(r,c):
            for i in range(r-1,-1,-1):
                if chess[i][c]=='Q':
                    return True
            i,j=r-1,c+1
            temp=1
            while i>=0 and j<n:
                if chess[i][j]=='Q':
                    return True
                i-=1
                j+=1
                temp+=1
            temp=0
            i,j=r-1,c-1
            while i>=0 and j>=0:
                if chess[i][j]=='Q':
                    return True
                i-=1
                j-=1
                temp+=1
            return False
        def build(r):
            if r==n:
                result[0]=result[0]+1
                return 
            else:
                for i in range(n):
                    if conflict(r,i):
                        continue
                    chess[r][i]='Q'
                    build(r+1)
                    chess[r][i]='.'
        build(0)
        return result[0]
        