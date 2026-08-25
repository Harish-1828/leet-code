# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        n-=1
        if n==0 and head.next is None:
            return None
        temp2=temp
        while n!=0:
            temp2=temp2.next
            n-=1
        if temp is None:
            return None
        prev=temp
        while temp2.next is not None:
            prev=temp
            temp=temp.next
            temp2=temp2.next
        print(prev.val)
        print(temp.val)
        print(temp2.val)
        prev.next=temp.next
        if prev == temp:
            return head.next
        return head
