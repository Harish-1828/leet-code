class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r=len(matrix)
        c=len(matrix[0])
        result=[[0]*r for i in range(c)]

        for i in range(r):
            for j in range(c):
                result[j][i]=matrix[i][j]
        return result
        