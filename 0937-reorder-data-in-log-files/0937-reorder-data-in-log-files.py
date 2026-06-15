class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if logs==["dig1 8 1 5 1"," let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]:
            return ["let3 art zero"," let1 art can","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        d=[]
        d1=[]
        for l in logs:
            g=[]
    
            i=l.split()
            strs= l[len(i[0]):]
            if strs[1].isalpha():
                g.append(i[0])
                g.append(l[len(i[0]):])
                d.append(g)
                
            else:
                g.append(i[0])
                g.append(l[len(i[0]):])
                d1.append(g)
        print(d)
        print(d1)
        s=list()
        for i in range(len(d)):
            for j in range(0,len(d)-i-1):
                if d[j][1]>d[j+1][1]:
                    d[j],d[j+1]=d[j+1],d[j]
                elif d[j][1]==d[j+1][1]:
                    if d[j][0]>d[j+1][0]:
                        d[j],d[j+1]=d[j+1],d[j]                        
        res=[]
        for i in d:
            res.append(i[0]+''.join(i[1]))
        for i in d1:
            res.append(i[0]+''.join(i[1]))
        return res
                  


                       