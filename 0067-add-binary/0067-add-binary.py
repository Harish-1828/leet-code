class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=int(a,2),int(b,2)
        while b:
            w_carry=a^b
            carry=(a&b)<<1
            b,a=carry,w_carry
        return bin(a)[2:]