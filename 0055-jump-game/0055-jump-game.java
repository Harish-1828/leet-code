class Solution {
    public boolean canJump(int[] nums) {
        int max_steps=0;
        int curr=0;
      
        for(int i=0;i<nums.length-1;i++)
        {
            if(i>max_steps)
            {
                return false;
            }
            curr=i+nums[i];
         
            max_steps=Integer.max(curr,max_steps);
            System.out.print(max_steps);
        }
        if(max_steps>=nums.length-1)
        {
            return true;
        }
        return false;
    }
}