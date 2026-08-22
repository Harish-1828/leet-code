class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        prefix=[-1]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        dp={}
        if k==1:
            return prefix[-1]
        def fn(idx,curr_k):
            if (idx,curr_k) in dp:
                return dp[(idx,curr_k)]
            if curr_k==k-1:
                if idx == 0:
                    dp[(idx,curr_k)]=prefix[idx]
                    return prefix[idx]
                else:
                    dp[(idx,curr_k)]=prefix[-1] - prefix[idx-1]
                    return prefix[-1] - prefix[idx-1]
            else:
                res=float('inf')
                end = len(nums) - (k - curr_k - 1) #5-(2-1-1)
                for i in range(idx,end):
                    if idx == 0:
                        left = prefix[i]
                    else:
                        left = prefix[i] - prefix[idx-1]
                    right=fn(i+1,curr_k+1)
                    s=max(left,right)
                    res=min(res,s)
                dp[(idx,curr_k)]=res
                return res
        return fn(0,0)

        