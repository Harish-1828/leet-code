class Solution {
    public void rotate(int[][] matrix) {
        for(int i=0;i<matrix[0].length;i++)
        {
            for(int j=i+1;j<matrix.length;j++)
            { 
                int temp=matrix[i][j];
                matrix[i][j]=matrix[j][i];
                matrix[j][i]=temp;
            }
            for(int j=0,k=matrix.length-1;j<k;j++,k--)
            {
                int temp=matrix[i][k];
                matrix[i][k]=matrix[i][j];
                matrix[i][j]=temp;
            }

        }
    }
}