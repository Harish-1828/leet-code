class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sums=0
        str_1=str(num)
        n=len(str_1)
        if n==1:
            return num
        while len(str_1)>=2:
            sums=sum([int(i) for i in str_1])
            str_1=str(sums)
        return sums
        