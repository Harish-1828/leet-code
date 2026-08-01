class Solution {
    public int minimumPushes(String word) {
        int k=8;
        int push=0;
        int l=1;
        for(int i=0;i<word.length();i++)
        {
            if(i<k)
            {
                push=push+l;
            }
            else
            {
                k=k+8;
                l=l+1;
                push=push+l;
            }
        }
        return push;
    }
}