class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]
        def backtrack(i):
            if sum(path)>target or len(candidates)==i:
                return
            if sum(path)==target:
                result.append(path[:])
                return 
            backtrack(i+1)
            path.append(candidates[i])
            backtrack(i)
            path.pop()
        backtrack(0)
        return result 