class Solution {
    public int diagonalSum(int[][] mat) {
        int leftSum=0;
        int rightSum=0;
        int col=0;
        for(int row=0;row<mat.length;row++)
        {
            rightSum+=mat[row][col];
            mat[row][col]=0;
            col++;
        }
        col=mat[0].length-1;
        for(int row=0;row<mat.length;row++)
        {
            leftSum+=mat[row][col--];
        }
        return leftSum+rightSum;
        
    }
}