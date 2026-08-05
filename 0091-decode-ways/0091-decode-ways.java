class Solution {
     int[] dp;
    public  int fn(int i,String s)
    {
        if(i<s.length() && s.charAt(i)=='0')
            {
                return 0;
            }
        if(i>=s.length()-1)
        {
            return 1;
        }
        if(dp[i]!=-1)
        {
            return dp[i];
        }
        else
        {
            int takeOne =fn(i+1,s);
            int ans=0;
            int takeTwo=0;
            if(i+1<s.length())
            {
                ans=(ans*10)+(s.charAt(i)-'0');                ans=(ans*10)+(s.charAt(i+1)-'0');
                if(ans<=26)
                {
                    takeTwo=fn(i+2,s);
                }
            }
            dp[i]=takeOne+takeTwo;
            return dp[i];
        }
    }
    public int numDecodings(String s) {
        dp = new int[s.length()];
        Arrays.fill(dp, -1);
        return fn(0,s);
    }
}