class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0,0,0]
        for i in nums:
            count[i]=count[i]+1
        
        result=nums[:]
        print(result)
        for i in range(1,3):
            count[i]=count[i-1]+count[i]
        for i in result:
            count[i]=count[i]-1
            nums[count[i]]=i


