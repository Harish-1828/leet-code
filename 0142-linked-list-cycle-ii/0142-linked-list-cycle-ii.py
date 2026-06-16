# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def length(head):
            f = s = head

            while f and f.next:
                f = f.next.next
                s = s.next

                if f == s:
                    l = 1
                    s = s.next

                    while f != s:
                        s = s.next
                        l += 1

                    return l

            return 0

        l = length(head)

        if l == 0:
            return None

        first = second = head

        for _ in range(l):
            second = second.next

        while first != second:
            first = first.next
            second = second.next

        return first