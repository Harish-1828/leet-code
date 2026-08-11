class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = nums[0]

        # Find sequential prefix
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break

        # Find smallest number >= sum that is not in nums
        while s in nums:
            s += 1

        return s