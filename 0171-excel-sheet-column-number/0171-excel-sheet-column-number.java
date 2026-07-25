class Solution {
    public int titleToNumber(String str) {
        int num=0;
        int count=0;
        int ans=0;
        for(int i=str.length()-1;i>=0;i--)
        {
            int idx=(str.charAt(i)-'A')+1;
            ans = ans + (idx * (int)Math.pow(26, count++));   
     }
        return ans;
    }
}