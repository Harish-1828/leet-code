class Solution:
    def binaryGap(self, n: int) -> int:
        binary=bin(n)[2:]
        print(binary)
        start=0
        end=len(binary)-1
        lens=len(binary)
        longs=float('-inf')
        bit=n.bit_count()
        if bit==1:
            return 0
        while start<lens:
            l=start
            r=end
            if binary[l]=='0':
                start=start+1
                continue
            while (binary[l]!=binary[r]) or (binary[l]==binary[r]  and binary[l:r].count('1')>1):
                r=r-1
            print(l,r)
            c_long=(r-l)
            print(c_long)
            longs=max(c_long,longs)
            start=start+1
        return (longs)

            
