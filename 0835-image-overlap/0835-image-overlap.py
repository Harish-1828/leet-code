class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def get_number_ones(img1,img2):
            res1=[]
            res2=[]
            for i in range(len(img1)):
                for j in range(len(img1)):
                    if img1[i][j]==1:
                        res1.append((i,j))
                    if img2[i][j]==1:
                        res2.append((i,j))
            return res1,res2
        res1,res2=get_number_ones(img1,img2)
        d=defaultdict(int)
        m=0
        for i in range(len(res1)):
            for j in range(len(res2)):
                sub1=res1[i][0]-res2[j][0]
                sub2=res1[i][1]-res2[j][1]
                d[(sub1,sub2)]+=1
                if d[(sub1,sub2)]>m:
                    m=d[(sub1,sub2)]
        
        return m


        