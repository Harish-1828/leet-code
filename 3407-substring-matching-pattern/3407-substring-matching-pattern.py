class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        if p=='*':
            return True
   
        res=p.split('*')
        idx1=s.find(res[0])
        q=idx1+len(res[0])
        idx2=s[q:].find(res[1])
        if res[0]=='' and res[1]=='':
            print(1)
            return True
        if res[0]=='' and idx2==-1:
            print(2)
            return False
        if res[1]=='' and idx1==-1:
            print(3)
            return False
        if (idx1==-1 and idx2!=-1) or (idx1!=-1 and idx2==-1):
            print(4)
            return False
        if idx1==-1 and idx2==-1:
            print(5)
            return False
        return True 

        