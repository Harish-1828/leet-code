class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chess=[['.']*n for i in range(n)]
        print(chess)
        res=[0]
        result=[]
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
                result.append(["".join(row) for row in chess])
                return 
            else:
                for i in range(n):
                    if conflict(r,i):
                        continue
                    chess[r][i]='Q'
                    build(r+1)
                    chess[r][i]='.'
        build(0)
        return result


            
            





        