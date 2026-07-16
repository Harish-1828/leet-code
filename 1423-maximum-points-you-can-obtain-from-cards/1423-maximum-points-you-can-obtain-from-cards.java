class Solution {
    public int maxScore(int[] arr, int k) {
        int i=k-1;
        int lsum=0,rsum=0;
        int j=arr.length-1;
        for(int q=0;q<k;q++)
        {
             lsum+=arr[q];
        }
        int m=lsum;
         System.out.println(i);
        while(i>=0)
        {
            lsum=lsum-arr[i];
            rsum=rsum+arr[j];
            m=Integer.max(m,lsum+rsum);
            i--;
            j--;
        }
        return m;

        }
    }
