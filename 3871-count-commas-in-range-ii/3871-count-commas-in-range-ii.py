class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        if n >= 10**15:
            res += 5 * (n - 10**15 + 1)
            n = 10**15 - 1
        if n >= 10**12:
            res += 4 * (n - 10**12 + 1)
            n = 10**12 - 1
        if n >= 10**9:
            res += 3 * (n - 10**9 + 1)
            n = 10**9 - 1
        if n >= 10**6:
            res += 2 * (n - 10**6 + 1)
            n = 10**6 - 1
        if n >= 10**3:
            res += n - 10**3 + 1
        return res