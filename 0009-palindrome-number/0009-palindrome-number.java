class Solution {
    public boolean isPalindrome(int x) {
        if(x<0)
        {
            return false;
        }
        int cpy=x;
        int newnum=0;
        int ans=0;
        while(cpy>0)
        {
            int temp1=cpy%10;
            ans=(ans*10)+temp1;
            cpy/=10;
        }
        if(ans==x)
        {
            return true;
        }
        return false;
    }
}