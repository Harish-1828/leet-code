class Solution {
    public int maxProfit(int[] prices) {
        int profit=Integer.MIN_VALUE;
        int min_price=prices[0];
        for(int i=1;i<prices.length;i++)
        {
            int curr_profit=prices[i]-min_price;
            min_price=Integer.min(prices[i],min_price);
            profit=Integer.max(curr_profit,profit);
        }
        return (profit>0?profit:0);
    }
}