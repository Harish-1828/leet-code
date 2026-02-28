class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                bit_counti=arr[i].bit_count()
                bit_countj=arr[j].bit_count()
                if bit_counti>bit_countj:
                    arr[i],arr[j]=arr[j],arr[i]
                elif bit_counti==bit_countj and arr[i]>arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
                else:
                    continue
        return arr