from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()
        n = len(candidates)
        def back(i, r):
            if r == 0:
                res.append(path[:])
                return
            if i == n or r < 0:
                return
            j = i
            while j + 1 < n and candidates[j] == candidates[j + 1]:
                j += 1
            back(j + 1, r)
            path.append(candidates[i])
            back(i + 1, r - candidates[i])
            path.pop()

        back(0, target)
        return res