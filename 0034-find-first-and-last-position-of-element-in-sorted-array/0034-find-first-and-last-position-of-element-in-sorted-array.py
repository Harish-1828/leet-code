class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(st,end,first):
            ans=-1
            while st<=end:
                mid=(st+end)//2
                if nums[mid]>target:
                    end=mid-1
                elif nums[mid]<target:
                    st=mid+1
                else:
                    ans=mid
                    if first:
                        end=mid-1
                    else:
                        st=mid+1

            return ans
        index=find(0,len(nums)-1,True)
        i=find(0,len(nums)-1,False)
        return [index,i]
