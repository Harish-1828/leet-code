class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        for i in range(left,right+1):
            num=i.bit_count()
            flag=True
            print(num)
            if num==0 or num==1:
                continue
            for i in range(2,int(math.sqrt(num))+1):
                if num%i==0:
                    flag=False
                    break
            if flag:
                count=count+1
        return count 

        