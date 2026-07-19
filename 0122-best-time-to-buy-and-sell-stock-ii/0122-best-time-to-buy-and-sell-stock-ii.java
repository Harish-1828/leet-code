class Solution {
    int[][] dp;

    public int fn(int n, boolean buy, int[] prices)
    {
        if(n == prices.length)
        {
            return 0;
        }

        if(dp[n][buy ? 1 : 0] != -1)
        {
            return dp[n][buy ? 1 : 0];
        }

        if(buy)
        {
            int sell = prices[n] + fn(n + 1, false, prices);
            int notsell = fn(n + 1, true, prices);
            dp[n][1] = Integer.max(sell, notsell);
            return dp[n][1];
        }
        else
        {
            int bought = -prices[n] + fn(n + 1, true, prices);
            int not_bought = fn(n + 1, false, prices);
            dp[n][0] = Integer.max(bought, not_bought);
            return dp[n][0];
        }
    }

    public int maxProfit(int[] prices) {
        dp = new int[prices.length][2];
        for(int i = 0; i < prices.length; i++)
        {
            Arrays.fill(dp[i], -1);
        }
        return fn(0, false, prices);
    }
}