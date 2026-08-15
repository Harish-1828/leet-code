class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d={}
        row=len(board)
        col=len(board[0])
        for i in range(row):
            for j in range(col):
                count_1=0
                for x in range(-1,2):
                    for y in range(-1,2):
                        if x==0 and y==0:
                            continue
                        if 0<=(x+i)<row and 0<=(y+j)<col:
                            if board[i+x][j+y]!=0:
                                count_1+=1
                         
                d[(i,j)]=count_1
        key=d.keys()
        for i,j in key:
            one = d[(i,j)]
            if board[i][j]==1:
                if one<2 or one >3:
                    board[i][j]=0
            else:
                if one==3:
                    board[i][j]=1

        
                

   

        
        