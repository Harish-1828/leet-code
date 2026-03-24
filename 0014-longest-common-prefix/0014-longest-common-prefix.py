class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s1=strs[0]
        s2=strs[len(strs)-1]
       # s=s1.intersection(s2)
        l1=len(s1)
        l2=len(s2)
        i,j=0,0
        s=""
        while i<l1 and j<l2:
            if s1[i]==s2[j]:
                s=s+s1[i]
            else:
                break
            i+=1
            j+=1
        return s
            