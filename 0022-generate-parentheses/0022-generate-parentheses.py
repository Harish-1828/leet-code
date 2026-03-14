class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open=0 
        close=0
        res=[]
        path=[]
        def back(open,close):
            if open==close:
                res.append(path[:])
                return
            if open==n or close==n:
                return
            path.append('(')
            back(open+1,close)
            path.append(')')
            back(open,close+1)
            path.pop()

        