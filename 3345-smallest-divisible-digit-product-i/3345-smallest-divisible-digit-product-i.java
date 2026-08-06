class Solution {
    public static int fn(int num)
    {
        int res=1;
        while(num>0)
        {
            res=res*(num%10);
            num=num/10;
        }
        return res;
    }
    public int smallestNumber(int n, int t) {
        int res;
        System.out.print(fn(23));
        int i=n;
       while(true)
        {
            if(fn(i)%t==0)
            {
                return i;
            }
            i+=1;
        }
    }
}