class Solution:

    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        arr = set(forbidden)
        counts = [9999999]
        visited = set()
        limit = max(max(forbidden, default=0), x) + a + b
        def fn(idx, state, count):
            if idx < 0 or idx > limit:
                return
            if idx == x:
                counts[0] = min(counts[0], count)
                return
            if count >= counts[0]:
                return
            if (idx, state) in visited:
                return
            visited.add((idx, state))
            if idx + a <= limit and idx + a not in arr:
                fn(idx + a, True, count + 1)
            if state and idx - b >= 0 and idx - b not in arr:
                fn(idx - b, False, count + 1)
        fn(0, True, 0)
        if counts[0] == 9999999:
            return -1
        return counts[0]