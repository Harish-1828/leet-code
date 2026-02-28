class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0 or n<0:
            return False
        x=math.log2(n)
        if floor(x)==x:
            return True
        return False        