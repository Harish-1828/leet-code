class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=set()
        nums.sort()
        n=len(nums)
        for i in range(n):
            l=i+1
            r=n-1
            while l<r:
                sums=nums[i]+nums[l]+nums[r]
                if sums==0:
                    result.add((nums[i],nums[l],nums[r]))
                    l=l+1
                    r=r-1
                elif sums>0:
                    r=r-1
                else:
                    l=l+1
        r=[]
        for i in result:
            s=list(i)
            r.append(s)
        return r