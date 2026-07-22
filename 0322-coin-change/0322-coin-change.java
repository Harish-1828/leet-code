class Solution {
    int dp[][];
   public  int fn(int coins[],int idx,int remaining)
    {
      if (idx == coins.length)
        return 999999;

        if (remaining == 0)
            return 0;

        if (remaining<0)
            return 999999;

        if (dp[idx][remaining] != -1)
            return dp[idx][remaining];
        else
        {
            int take=1+fn(coins,idx,remaining-coins[idx]);
            int notake=fn(coins,idx+1,remaining);
            dp[idx][remaining]=Integer.min(take,notake);
            return dp[idx][remaining];
        }
    }
    public int coinChange(int[] coins, int amount) {
        dp = new int[coins.length][amount + 1];
        for (int i = 0; i < coins.length; i++)
        {
            Arrays.fill(dp[i], -1);
        }
        int x= fn(coins,0,amount);
        if(x==999999)
        {
            return -1;
        }
        return x;
    }
}