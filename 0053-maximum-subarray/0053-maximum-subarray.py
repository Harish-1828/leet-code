class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c,g=0,float('-inf')
        for i in nums:
            temp=c+i
            if temp<i:
                c=i
            else:
                c=temp
            g=max(c,g)
        return g