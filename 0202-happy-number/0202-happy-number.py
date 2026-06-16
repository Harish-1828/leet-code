class Solution:
    def isHappy(self, n: int) -> bool:
        def sums(n):
            ans=0
            while n>0:
                copy=n%10
                ans=pow(copy,2)+ans
                n=n//10
            return ans
        slow=n
        fast=n
        while True:
            slow=sums(slow)
            fast=sums(sums(fast))
            if fast==1:
                return True
            if slow==fast:
                return False
        return True     