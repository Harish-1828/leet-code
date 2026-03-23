class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        d=defaultdict(int)
        count=1
        for i in nums:
            d[count]=i
            count+=1
        def backtrack(path):
            if len(path)==len(nums):
                result.append(path[:])
                return
            else:
                for i in d.keys():
                    if i not in path:
                        path.append(i)
                        backtrack(path)
                        path.pop()
        backtrack([])
        res=set()
        for i in result:
            paths=[]
            for j in i:
                paths.append(d[j])
            res.add(tuple(paths[:]))
        return list(res)

    