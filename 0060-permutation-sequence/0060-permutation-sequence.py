class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l=[str(i) for i in range(1,n+1) ]
        N=len(l)
        res=[]
        x=[0]
        def back(path):
            if len(path)==N:
                res.append(path[:])
                x[0]=x[0]+1
                return
            if x[0]==k:
                res.append(path[:])
                return -1
            else:
                for i in l:
                    if i not in path:
                        path.append(i)
                        back(path)
                        path.pop()
        back([])
        return "".join(res[k-1])
