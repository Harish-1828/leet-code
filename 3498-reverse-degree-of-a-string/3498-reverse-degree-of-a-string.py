class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for index,i in enumerate(s):
            a_index=(ord(i)-ord('a'))
            z_index=ord('z')-ord('a')
            idx=(((z_index-a_index))%26)+1
            ans=ans+((index+1)*idx)
        return ans
   
