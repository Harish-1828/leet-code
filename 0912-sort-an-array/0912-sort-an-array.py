class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(list1):
            if len(list1)==1:
                return list1
            mid=len(list1)//2
            left=mergesort(list1[:mid])
            right=mergesort(list1[mid:])
            return merge(left,right)
        def merge(left,right):
            i,j,k=0,0,0
            l=[0]*(len(left)+len(right))
            while(len(left) > i and len(right) > j):
                if left[i]<right[j]:
                    l[k]=left[i]
                    i=i+1
                else:
                    l[k]=right[j]
                    j=j+1
                k=k+1
            while i<len(left):
                l[k]=left[i]
                k+=1
                i+=1
            while j<len(right):
                l[k]=right[j]
                j+=1
                k+=1
            return l
        return mergesort(nums)

