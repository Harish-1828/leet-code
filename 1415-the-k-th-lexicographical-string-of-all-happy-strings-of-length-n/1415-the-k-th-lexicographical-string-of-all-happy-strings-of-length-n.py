class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        list1=['a','b','c']
        result=[]
        def  back(path):
            if len(path)==n:
                flag=0
                for i in range(len(path)-1):
                    if path[i]==path[i+1]:
                        flag=flag+1
                        break
                if flag==0:
                    result.append(path[:])
                    return
                else:
                    return
                return 
            for i in list1:
                path.append(i)
                back(path)
                path.pop()
        back([])
        result.sort()
        try:
            return "".join(result[k-1])
        except:
            return ""
        