class Solution:
    def mySqrt(self, x: int) -> int:
        st,end=1,x
        while st<=end:
            m=(st+end)//2
            s=m*m
            if s==x:
                return m
            elif s<x:
                st=m+1
            else:
                end=m-1
        return end     