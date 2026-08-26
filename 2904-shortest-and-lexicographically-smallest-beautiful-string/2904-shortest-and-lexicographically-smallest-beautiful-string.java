class Solution {
    public String shortestBeautifulSubstring(String s, int k) {
        int i=0;
        int j=0;
        String sb="";
        int count_1=0 ;
        int len=Integer.MAX_VALUE;
        while(j<s.length())
        {
            if(s.charAt(j)=='1')
            {
                count_1++;
            }
            if(count_1>k)
            {
                while (i<s.length() && count_1>k)
                {
                    if(s.charAt(i)=='1')
                    {
                        count_1--;
                    }
                    i++;
                }
            }
            if (count_1==k)
            {
                while(i<s.length() && s.charAt(i)=='0')
                {
                    i++;
                }
                String candidate = s.substring(i, j + 1);
                if ((j - i + 1) < len ||((j - i + 1) == len && candidate.compareTo(sb) < 0))
                {
                    len = j - i + 1;
                    sb = candidate;
                }
            }
            j++;
        }
        return sb;
    }
}