import re
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s1= s.index('1')
        try:
            s2=s.index('0')
        except:
            return True
        print(s1)
        Flag=True
        for i in range(s2+1,len(s)):
            if s[i]=='1':
                return False
        return True


