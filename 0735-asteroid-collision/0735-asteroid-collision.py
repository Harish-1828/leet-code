class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        i=0
        while i<len(arr):
            if (i+1<len(arr)) and (arr[i]>0 and arr[i+1]>0):
                i+=1
            elif (i+1<len(arr)) and (arr[i+1]>0 and arr[i]<0):
                i+=1
            elif (i+1<len(arr)) and ((abs(arr[i]))==abs(arr[i+1])):
                if arr[i]>0 and arr[i+1]<0:
                    arr.pop(i)
                    arr.pop(i)
                    if i>0:
                        i-=1
                else:
                    i+=1
            elif (i+1<len(arr)) and (arr[i]>0 and arr[i+1]<0):
                if abs(arr[i])<abs(arr[i+1]):
                    arr.pop(i)
                else:
                    arr.pop(i+1)
                if i==0:
                    continue
                i-=1
            else:
                i+=1

        return arr
        