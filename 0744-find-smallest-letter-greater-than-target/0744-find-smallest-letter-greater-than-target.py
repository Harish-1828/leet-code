class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        st=0
        end=len(letters)-1
        while st<=end:
            mid=st+(end-st)//2
            if letters[mid]<=target:
                st=mid+1
            else:
                end=mid-1
        return letters[st %len(letters) ]