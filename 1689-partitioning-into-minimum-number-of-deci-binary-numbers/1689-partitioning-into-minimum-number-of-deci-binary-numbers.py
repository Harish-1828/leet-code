class Solution:
    def minPartitions(self, n: str) -> int:
        n1=set(n)
        res=[int(i) for i in n1]
        return max(res)
    
       

        