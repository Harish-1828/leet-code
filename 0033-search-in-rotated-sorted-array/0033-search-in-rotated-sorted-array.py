class Solution:
    def search(self, nums, target):
        def find(s, e):
            if s > e:
                return -1
            
            mid = (s + e) // 2
            
            if nums[mid] == target:
                return mid
            if nums[s] <= nums[mid]:
                if nums[s] <= target < nums[mid]:
                    return find(s, mid - 1)
                else:
                    return find(mid + 1, e)            
            else:
                if nums[mid] < target <= nums[e]:
                    return find(mid + 1, e)
                else:
                    return find(s, mid - 1)
        
        return find(0, len(nums) - 1)