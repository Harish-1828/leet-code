class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=1
        n=len(nums)

        while i<=k:
            ele=nums.pop()
            nums.insert(0,ele)
            i=i+1
        


        