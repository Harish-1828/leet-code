class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtrack(start_index, path):
            if len(path) == k and sum(path) == n:
                result.append(path[:])
                return
            if sum(path) > n or len(path) > k:
                return
            for num in range(start_index, 10):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()
        backtrack(1, [])
        return result
