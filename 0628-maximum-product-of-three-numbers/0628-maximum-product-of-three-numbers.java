class Solution {
    public int maximumProduct(int[] arr) {
        int max1=-99999,max2=-99999,max3=-22222;
        int min1=99999, min2=99999;
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]>max1)
            {
                max3=max2;
                max2=max1;
                max1=arr[i];
            }
            else if(arr[i]>max2)
            {
                max3=max2;
                max2=arr[i];
            }
            else if(arr[i]>max3)
            {
                max3=arr[i];
            }
            if(arr[i]<min1)
            {
                min2=min1;
                min1=arr[i];
            }
            else if(arr[i]<min2)
            {
                min2=arr[i];
            }
        }
        int num1=max1*max2*max3;
        int num2=min1*min2*max1;
        return Integer.max(num1,num2);
    }
}