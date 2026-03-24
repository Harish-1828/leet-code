class Solution:
    def countAndSay(self, n: int) -> str:
        def counts(n):
            if n==1:
                return "1"
            else:
                string=counts(n-1)
                r=helper(string)
                s=joins(r)
                return s
        def helper(s):
            result=[]
            i=0
            while i<len(s):
                lis=[]
                count=0
                j=i
                while j<len(s) and s[i]==s[j]:
                    count+=1
                    j+=1
                lis.append(str(count))
                lis.append(s[i])
                i+=count
                result.append(lis[:])
            return result       
        def joins(l):
            s=""
            for i in l:
                s=s+"".join(i)
            return s
        return counts(n)