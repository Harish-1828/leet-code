class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=0
        fin=[]
        n=len(s)
        for i in range(n):
            if s[i]=='(':
                if res>0:
                    fin.append(s[i])
                res+=1
            else:
                res-=1
                if res>0:
                    fin.append(s[i])
        return ''.join(fin)