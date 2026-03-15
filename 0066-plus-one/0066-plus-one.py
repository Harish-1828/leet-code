class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp=0
        n=len(digits)
        l=[]
        for i in range(n):
            temp=temp+(digits[i]*pow(10,n-i-1))
        return list(map(lambda x: int(x),list(str(temp+1))))
        
        
        