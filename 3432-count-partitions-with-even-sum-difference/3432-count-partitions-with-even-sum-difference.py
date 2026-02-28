class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        c_count=0
        l1=[]
        l2=[]
        l2=nums.copy()
        for i in range(0,len(nums)-1):
            if len(nums)==1:
                    break
            l1.append(nums[i])
            l2.remove(nums[i])
            sum1=sum(l1)
            sum2=sum(l2)
            print(l1,l2)
            diff=abs(sum1-sum2)
            print(diff)
            if diff%2==0:
                c_count=c_count+1
        return c_count
        