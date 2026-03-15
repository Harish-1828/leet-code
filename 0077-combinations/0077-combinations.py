class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        r=[x for x in range(1,n+1)]
        res,path=[],[]
        def back(i):
            if len(path)==k:
                res.append(path[:])
                return
            if i==n:
                return
            back(i+1)
            path.append(r[i])
            back(i+1)
            path.pop()
        back(0)
        return res