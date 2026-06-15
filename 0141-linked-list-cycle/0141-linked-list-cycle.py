class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turbo = head
        slow = head

        while turbo and turbo.next:
            turbo = turbo.next.next
            slow = slow.next

            if turbo == slow:
                return True
            
        return False
        