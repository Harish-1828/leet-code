class Solution:
    def numberOfSteps(self, num: int) -> int:
        def counts(n,s):
            if n==0:
                return s
            else:
                if n%2==0:
                    return counts(n//2,s+1)
                return counts(n-1,s+1)
        return counts(num,0)        