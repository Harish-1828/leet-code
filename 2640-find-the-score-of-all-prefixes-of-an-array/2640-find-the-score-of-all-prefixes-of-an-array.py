class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        print(prefix)
        ans=0
        res=[]
        for i in range(1,len(nums)):
            prefix[i]=max(prefix[i-1],nums[i])
        res=[]
        ans=0
        for i in range(len(nums)):
            s=nums[i]+prefix[i]
            ans=ans+s
            res.append(ans)
        return res