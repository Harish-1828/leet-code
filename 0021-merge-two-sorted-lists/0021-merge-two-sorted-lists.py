# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp3=ListNode()
        c=temp3
        temp1=list1
        temp2=list2
        while temp1 is not None and temp2 is not None:
            if temp1.val>temp2.val:
                c.next=temp2
                temp2=temp2.next
            else:
                c.next=temp1
                temp1=temp1.next
            c=c.next
        if temp1:
            c.next=temp1
        else:
            c.next=temp2
        return temp3.next
