class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        s=0
        i=0
        cost.sort(reverse=True)
        if len(cost)==1:
            return cost[0]
        while i<len(cost):
            if i+1>=len(cost):
                s=s+cost[i]
                break
            s=s+cost[i]+cost[i+1]
            i+=3
        return s
