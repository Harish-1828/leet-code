class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=0
        fin=""
        temp=""
        for i in range(len(s)):
            if s[i]=='(':
                temp+=s[i]
                res+=1
            else:
                temp+=s[i]
                res-=1
            if res==0:
                fin+=temp[1:len(temp)-1]
                temp=""
        return fin