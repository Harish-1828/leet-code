class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=[]
        r=[]
        def back(open,close):
            if open==close==n:
                print(l)
                r.append("".join(l))
                return
            if open<n:
                l.append('(')
                back(open+1,close)
                l.pop()
            if close<open:
                l.append(')')
                back(open,close+1)
                l.pop()
            return
        back(0,0) 
        return r