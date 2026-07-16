class Solution {
    public int longestOnes(int[] nums, int k) {
        int zerocount=0;
        int i=0;
        int j=0;
        int m=0;
        while(j<nums.length)
        {
            if(nums[j]==0)
            {
                zerocount++;
            }
            if(zerocount<=k)
            {
                      m=Integer.max(m,j-i+1);
            }
            if(zerocount>k)
            {
                while(zerocount>k)
                {
                    if(nums[i]==0){
                        zerocount--;
                    }
                    i++;
                }
            }
            j++;
        }
        return m;
    }
}