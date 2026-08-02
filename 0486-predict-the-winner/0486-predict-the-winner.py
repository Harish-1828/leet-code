class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        d=defaultdict()
        def fn(i,j):
            if (i,j) in d:
                return d[(i,j)]
            elif i==j:
                d[(i,j)]=nums[j]
                return nums[j]
            else:
                takeFirst=nums[i]-fn(i+1,j)
                takeSecond=nums[j]-fn(i,j-1)
                d[(i,j)]= max(takeFirst,takeSecond)
                return d[(i,j)]
        if fn(0,len(nums)-1)<0:
            return False
        return True
        