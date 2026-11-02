class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m=min(nums)
        moves=0
        for i in nums:
            if i!=m:
                moves+=i-m
        return moves