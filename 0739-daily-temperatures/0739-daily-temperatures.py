class Solution:
    def dailyTemperatures(self, arr: list[int]) -> list[int]:
        st=[]
        res=[0]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            while st and arr[st[-1]]<=arr[i]:
                st.pop()
            if not st:
                res[i]=0
            else:
                res[i]=st[-1]-i
            st.append(i)
        return res

        