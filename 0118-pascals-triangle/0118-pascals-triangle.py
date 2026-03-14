class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows ==1:
            return [[1]]
        result=[[1],[1,1]]
        list1=[]
        sums=0
        for i in range(2,numRows):
            list1=[]
            list1.append(1)
            for j in range(i-1):
                sums=sums+sum(result[-1][j:j+2])
                list1.append(sums)
                sums=0
            list1.append(1)
            result.append(list1)
        return result
        