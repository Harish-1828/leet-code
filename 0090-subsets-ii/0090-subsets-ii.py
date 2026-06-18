class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        def fn(p,up):
            if len(up)==0:
                p.sort()
                ans.add(tuple(p[:]))
                return
            else:
                fn(p+[up[0]],up[1:])
                fn(p,up[1:])
        fn([],nums)
        res=[]
        for i in ans:
            res.append(list(i))
        return res
        
