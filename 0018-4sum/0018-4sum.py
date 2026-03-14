class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result=set()
        for i in range(len(nums)-3):
            s=0
            for j in range(i+1,n):
                l=j+1
                r=n-1
                while l<r:
                    s=nums[l]+nums[r]+nums[i]+nums[j]
                    if s==target:
                        result.add((nums[i],nums[j],nums[l],nums[r]))
                        l=l+1
                        r=r-1
                    elif s>target:
                        r=r-1
                    else:
                        l=l+1
        return list(map(lambda x:list(x),result))