class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l,r=[],[]
        for i in range(len(nums)-1):
            s=sum(nums[i+1:])
            r.append(s)
        r.append(0)
        for i in range(len(nums)):
            s=sum(nums[:i])
            l.append(s)
        return list(map(lambda x,y:abs(y-x),l,r))