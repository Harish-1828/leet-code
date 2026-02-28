class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        choice=[None]*n
        half_len=(n+1)//2
        pos_mod=defaultdict(lambda :[0]*(n+1))
        for d in range(10):
            pos_mod[d][0]=d%k
        for d in range(10):
            for i in range(1,n):
                pos_mod[d][i]=(pos_mod[d][i-1]*10)%k

        @cache
        def dp(i, mod):
            if i == half_len:
                if mod == 0:
                    return True
                return False
            
            digit_pos = set([i, n - i - 1])
            
            for d in range(9, -1, -1):
                cur_mod = 0
                for pos in digit_pos:
                    choice[pos] = d
                    cur_mod += pos_mod[d][pos]
                
                if dp(i + 1, (cur_mod + mod) % k):
                    return True
            
            return False
        
        dp(0, 0)
        return ''.join(map(str,choice))