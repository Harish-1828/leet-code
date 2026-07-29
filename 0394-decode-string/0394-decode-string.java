class Solution {
    public String decodeString(String s) {
        int[] num=new int[s.length()];
        StringBuilder[] str=new StringBuilder[s.length()];
        int top=-1;
        int top2=-1;
        int ans=0;
        StringBuilder sb=new StringBuilder();
        for(char c:s.toCharArray())
        {
            if(Character.isDigit(c))
            {
                ans=ans*10+(c-'0');
                continue;
            }
            else if(c=='[')
            {
                str[++top]=sb;
                sb=new StringBuilder();
                num[++top2]=ans;
                ans=0;
            }
            else if(c==']')
            {
                StringBuilder temp=str[top--];
                int count=num[top2--];

                while(count!=0)
                {
                    temp.append(sb);
                    count--;
                }
                sb=temp;
            }
            else
            {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}