class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        vis=[-1]*len(digits)
        t=[0]
        def fn(num,p):
            used=set()
            if p==3:
                t[0]+=1
                return 
            else:
                for i in range(len(digits)):
                    if p==1 and num==0:
                        continue
                    if digits[i] not in used and vis[i]==-1:
                        if p==2 and digits[i]%2!=0:
                            continue
                        used.add(digits[i])
                        vis[i]=0
                        fn((num*10)+digits[i],p+1) 
                        vis[i]=-1
        fn(0,0)
        return t[0]