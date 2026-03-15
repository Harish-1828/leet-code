class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s=""
        for i in range(len(nums)):
            if nums[i][i]=="0":
                s=s+'1'
            else:
                s=s+'0'
        return s
        