# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow=head,head
        count =0
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            count+=1
            slow=slow.next
        if count ==0:
            return None
        temp=head
        while temp.next is not None and temp.next!=slow:
            temp=temp.next
        if slow.next is None:
            temp.next=None
            return head
        temp.next=slow.next
        return head