class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c)
     {
        int m=mat.length;
        int n=mat[0].length;
        if((m*n)!=(r*c))
        {
            return mat;
        }

        int[][] res=new int[r][c];
        int row=0;
        int col=0;
        for(int i=0;i<mat.length;i++)
        {
            for(int j=0;j<mat[0].length;j++)
            {
                if(col==c)
                {
               
                    row++;
                    col=0;
                }
                res[row][col++]=mat[i][j];
            }
        }
        return res;
    }
}