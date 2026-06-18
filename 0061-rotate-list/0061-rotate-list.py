# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if k==0:
            return head
        first=head
        count =0
        while first is not None:
            prev=first
            count=count+1
            first=first.next
        if k==count:
            return head
        new_last=head
        if count==1:
            return head
        k=(k)%count
        if k==0:
            return head
        new_last_index=(count-k)-1
        new_last=head
        while new_last_index!=0:
            new_last=new_last.next
            new_last_index-=1
        t=new_last.next
        new_last.next=None
        prev.next=head
        return t


        
       
