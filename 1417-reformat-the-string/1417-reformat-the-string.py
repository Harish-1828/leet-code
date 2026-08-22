class Solution:
    def reformat(self, s: str) -> str:
        d=[]
        a=[]
        for i in s:
            if i.isdigit():
                d.append(i)
            else:
                a.append(i)
        i=0
        j=0
        res=""
        while i<len(a) and j<len(d):
            if len(a)>len(d):
                res+=a[i]+d[j]
            else:
                res+=d[j]+a[i]
            i+=1
            j+=1
        if len(a)-len(d) not in [-1,0,1]:
            return ""
        if len(a)==len(d):
            return res
        if len(a)<len(d):
            res+=d[-1]
        else:
            res+=a[-1]
            
        return res
        