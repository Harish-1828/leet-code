class Solution {
    static HashMap<Integer,Integer> dp =new HashMap<>();
    public static int fn(int n)
    {
        if(dp.containsKey(n))
        {
            return dp.get(n);
        }
        else
        {
            dp.put(n,fn(n-1)+fn(n-2));
            return dp.get(n);
        }
    }
    public int fib(int n) {
        dp.put(0,0);
        dp.put(1,1);
        return fn(n);
    }
}