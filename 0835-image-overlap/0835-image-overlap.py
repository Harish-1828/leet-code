class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        res1=[]
        res2=[]
        l=len(img1)
        for i in range(l):
            for j in range(l):
                if img1[i][j]==1:
                    res1.append((i,j))
                if img2[i][j]==1:
                    res2.append((i,j))
        d=defaultdict(int)
        m=0
        l1=len(res1)
        l2=len(res2)
        for i in range(l1):
            for j in range(l2):
                sub1=res1[i][0]-res2[j][0]
                sub2=res1[i][1]-res2[j][1]
                d[(sub1,sub2)]+=1
                if d[(sub1,sub2)]>m:
                    m=d[(sub1,sub2)]
        return m


        