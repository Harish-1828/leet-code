class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        r=list(map(lambda x:x[::-1],l))
        return " ".join(r)

        