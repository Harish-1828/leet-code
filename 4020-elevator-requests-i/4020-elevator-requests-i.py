class Solution:
    def elevatorRequests(self, n: int, arr: list[int]) -> int:
        sec=0
        ans=arr[0]
        for i in range(1,len(arr)):
            ans=ans+abs(arr[i-1]-arr[i])
        return ans
