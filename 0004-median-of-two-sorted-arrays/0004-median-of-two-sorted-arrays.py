class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        num=nums1+nums2
        n=len(num)
        num.sort()
        print(num)
        if len(num)%2!=0:
            return num[n//2]
        else:
            sum= (num[n//2]+num[(n//2)-1])
        
            return float(sum/2)
        
        