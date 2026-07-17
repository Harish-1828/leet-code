class Solution {
    public int maxArea(int[] height) {
        int i=0;
        int j=height.length-1;
        int max=Integer.MIN_VALUE;
        int area=0;

        while(i<j)
        {
             area=Integer.min(height[i],height[j])*(j-i);
             max=Integer.max(area,max);
            if(height[i]<height[j])
            {
                i++;
            }
            else
            {
                j--;
            }
        }
        return max;
    }
}