class Solution:
    def minOperations(self, s: str) -> int:
        count1=0
        count2=0            
        n=len(s)
        s1=""
        s2=""
        for i in range(n):
                if i%2==0:
                    s1=s1+'0'
                    s2=s2+'1'
                else:
                    s1=s1+'1'
                    s2=s2+'0'
        if s==s1 or s==s2:
            return 0
        for i,j in zip(s,s1):
            if i!=j:
                count1=count1+1
        for i,j in zip(s,s2):
            if i!=j:
                count2=count2+1
        return min(count1,count2)

