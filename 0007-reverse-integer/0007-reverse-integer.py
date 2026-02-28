class Solution:
    def reverse(self, x: int) -> int:
        v=x
        n=len(str(v))
        n=n-1
        if x>0:
            copy=x
        else:
            copy=x*-1
            n=n-1
        sum_1=0
        while copy>0:
            last=copy%10
            sum_1=sum_1+(last*pow(10,n))
            n=n-1
            copy=copy//10
        if sum_1 < -2**31 or sum_1> 2**31 - 1:
            return 0
        elif x>0:
            return sum_1
        else:
            return sum_1*-1



