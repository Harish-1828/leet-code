class Solution:
    def longestPalindrome(self, s: str) -> str:
        i=0

        n=len(s)
        start=0
        end=0
        def c(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return r-l-1
        while i<len(s):
            odd=c(i,i)
            even=c(i,i+1)

            m=max(odd,even)
            if m > end - start:
                start = i - (m-1) // 2
                end = i + m // 2

            i+=1
        return s[start:end+1]
        