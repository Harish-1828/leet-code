class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        curr=0
        t={}
        for i in tasks:
            curr+=1
            if i in t and curr-t[i]<=space:
                curr+=space-(curr-t[i])+1
            t[i]=curr
        return curr
