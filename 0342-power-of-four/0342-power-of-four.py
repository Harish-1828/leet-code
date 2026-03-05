class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        c=math.log(n,4)
        print(c)
        if floor(c)==c:
            return True
        else:
            return False
        