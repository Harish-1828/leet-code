class Solution {
    public static int fn(int n)
    {
        int temp;
        int pro=1;
        int sum=0;
        while(n>0)
        {
            temp=n%10;
            sum+=temp;
            pro*=temp;
            n=n/10;
        }
        return pro+sum;
    }
    public boolean checkDivisibility(int n) {
     if(n%fn(n)==0)
     {
        return true;
     }
     return false;
    }
}