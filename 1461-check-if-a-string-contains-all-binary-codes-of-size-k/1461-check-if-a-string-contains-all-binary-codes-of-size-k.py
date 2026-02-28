class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        s1=set()
        r=pow(2,k)
        n=len(s)
        for i in range(n-k+1):
            s1.add(s[i:i+k])
        print(len(s1))
        if len(s1)==r:
            return True
        return False
        