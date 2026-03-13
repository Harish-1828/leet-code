class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=[]
        count=0
        for i in nums[:]:
            if i not in res:
                res.append(i)
                continue
            nums.remove(i)
            count=count+1
        