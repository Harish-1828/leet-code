# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, temp: Optional[ListNode]) -> bool:
        l=[]
        while temp is not None:
            l.append(temp.val)
            temp=temp.next
        if l==l[::-1]:
            return True
        return False
        