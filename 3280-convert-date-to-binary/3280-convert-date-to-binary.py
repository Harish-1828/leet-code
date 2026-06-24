class Solution:
    def convertDateToBinary(self, date: str) -> str:
        d=date.split('-')
     
        s=""
        for i in d:
            s=s+(bin(int(i)))[2::]
            s=s+'-'

        return s[:-1]
            
   